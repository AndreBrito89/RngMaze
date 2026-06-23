import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import copy

from Enemies.Enemy import Boss
from entity_generator import ENEMY_TEMPLATES, EnemyGenerator, create_hero_by_role
from game_logic import (
    attempt_player_escape,
    list_player_consumables,
    resolve_enemy_attack,
    resolve_player_attack,
    use_player_consumable,
)
from sprite_catalog import get_enemy_sprite_data


class ActionButton:
    def __init__(self, parent, text, command, bg, fg="#ffffff", disabled_fg="#cfcfcf"):
        self._command = command
        self._state = "normal"
        self._bg = bg
        self._fg = fg
        self._disabled_fg = disabled_fg
        self._text = text

        self.frame = tk.Frame(parent, bg=bg, bd=0, highlightthickness=0, height=44)
        self.frame.pack_propagate(False)
        self.canvas = tk.Canvas(self.frame, bg=bg, highlightthickness=0, bd=0, height=44)
        self.canvas.pack(fill="both", expand=True)

        self.frame.bind("<Configure>", self._on_resize)
        self.canvas.bind("<Configure>", self._on_resize)
        self.canvas.bind("<Button-1>", self._on_click)
        self.frame.bind("<Button-1>", self._on_click)

        self._redraw()

    def _on_resize(self, _event):
        self._redraw()

    def _redraw(self):
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, width, height, fill=self._bg, outline="")
        text_color = self._fg if self._state == "normal" else self._disabled_fg
        self.canvas.create_text(
            width // 2,
            height // 2,
            text=self._text,
            fill=text_color,
            font=("Consolas", 13, "bold"),
            anchor="center",
        )

    def _on_click(self, _event):
        if self._state == "normal" and self._command is not None:
            self._command()

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def config(self, **kwargs):
        if "state" in kwargs:
            self._state = kwargs["state"]

        if "bg" in kwargs:
            self._bg = kwargs["bg"]
            self.frame.config(bg=self._bg)

        if "text" in kwargs:
            self._text = kwargs["text"]

        self._redraw()

    def __getitem__(self, key):
        if key == "state":
            return self._state
        raise KeyError(key)


class DoomDungeonUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RngMaze - Doom Dungeon")
        self.geometry("1180x720")
        self.configure(bg="#0a0a0a")

        self.hero_role_key = "berserker"
        self.total_sectors = 5
        self.enemy_generator = EnemyGenerator()

        self.player = create_hero_by_role(self.hero_role_key, "DoomSlayer")
        self.enemies = self.enemy_generator.generate_campaign(self.total_sectors)
        self.enemy_index = 0
        self.current_enemy = self.enemies[self.enemy_index]
        self.inventory_slot_map = []
        self._resize_after_id = None
        self._enemy_flash_ticks = 0
        self._floating_texts = []
        self._enemy_anchor = (0, 0)
        self._player_anchor = (0, 0)
        self._enemy_lab_window = None
        self._sprite_editor_window = None
        self._secret_input_buffer = ""
        self._secret_code = "iddqd"
        self._runtime_sprite_catalog = {}

        self._build_layout()
        self._bind_shortcuts()
        self.after_idle(self._refresh_all)
        self.after(33, self._tick_effects)
        self._log("Bem-vindo ao setor infernal. Sobreviva aos corredores.")

    def _build_layout(self):
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.scene_canvas = tk.Canvas(
            self,
            bg="#050505",
            highlightthickness=1,
            highlightbackground="#861111",
        )
        self.scene_canvas.grid(row=0, column=0, sticky="nsew", padx=(14, 7), pady=14)
        self.scene_canvas.bind("<Configure>", self._on_scene_configure)

        right = tk.Frame(self, bg="#111111", highlightthickness=1, highlightbackground="#8f1313")
        right.grid(row=0, column=1, sticky="nsew", padx=(7, 14), pady=14)
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(3, weight=0)
        right.grid_rowconfigure(4, weight=0)

        title = tk.Label(
            right,
            text="DOOM DUNGEON HUD",
            bg="#111111",
            fg="#ff4d4d",
            font=("Consolas", 18, "bold"),
        )
        title.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 6))

        self.status_label = tk.Label(
            right,
            justify="left",
            anchor="w",
            bg="#111111",
            fg="#f0f0f0",
            font=("Consolas", 11),
        )
        self.status_label.grid(row=1, column=0, sticky="ew", padx=10)

        self.vitals_canvas = tk.Canvas(
            right,
            bg="#0c0c0c",
            highlightthickness=1,
            highlightbackground="#343434",
            height=84,
            relief="flat",
        )
        self.vitals_canvas.grid(row=2, column=0, sticky="ew", padx=10, pady=(6, 8))

        action_frame = tk.Frame(right, bg="#111111")
        action_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=(4, 8))
        action_frame.grid_rowconfigure(0, minsize=48, weight=0)
        action_frame.grid_columnconfigure(0, weight=1)
        action_frame.grid_columnconfigure(1, weight=1)
        action_frame.grid_columnconfigure(2, weight=1)

        self.attack_button = ActionButton(
            action_frame,
            text="ATACAR",
            command=self._on_attack,
            bg="#8f1313",
            disabled_fg="#ffd7d7",
        )
        self.attack_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.escape_button = ActionButton(
            action_frame,
            text="FUGIR",
            command=self._on_escape,
            bg="#5c2b00",
            disabled_fg="#ffe7c6",
        )
        self.escape_button.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

        self.next_button = ActionButton(
            action_frame,
            text="PROX. SALA",
            command=self._advance_room,
            bg="#1f4e21",
            disabled_fg="#d6ffd6",
        )
        self.next_button.config(state="disabled")
        self.next_button.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

        inventory_frame = tk.Frame(right, bg="#151515", highlightthickness=1, highlightbackground="#353535")
        inventory_frame.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 8))
        inventory_frame.grid_columnconfigure(0, weight=1)
        inventory_frame.grid_rowconfigure(1, weight=1)

        inventory_title = tk.Label(
            inventory_frame,
            text="INVENTARIO",
            bg="#151515",
            fg="#f4d35e",
            font=("Consolas", 12, "bold"),
        )
        inventory_title.grid(row=0, column=0, sticky="ew", pady=(6, 4))

        self.inventory_listbox = tk.Listbox(
            inventory_frame,
            bg="#0f0f0f",
            fg="#e7e7e7",
            selectbackground="#8f1313",
            selectforeground="#ffffff",
            relief="flat",
            font=("Consolas", 10),
            height=6,
        )
        self.inventory_listbox.grid(row=1, column=0, sticky="nsew", padx=6, pady=(0, 6))

        self.use_item_button = tk.Button(
            inventory_frame,
            text="USAR ITEM",
            command=self._on_use_selected_item,
            bg="#87600f",
            fg="#ffffff",
            activebackground="#a47412",
            activeforeground="#ffffff",
            relief="flat",
            font=("Consolas", 10, "bold"),
        )
        self.use_item_button.grid(row=2, column=0, sticky="ew", padx=6, pady=(0, 8))

        self.log_text = tk.Text(
            right,
            bg="#0b0b0b",
            fg="#d4d4d4",
            insertbackground="#d4d4d4",
            relief="flat",
            height=10,
            font=("Consolas", 10),
            state="disabled",
        )
        self.log_text.grid(row=5, column=0, sticky="nsew", padx=10, pady=(0, 10))
        right.grid_rowconfigure(5, weight=1)
        self.log_text.tag_configure("info", foreground="#d4d4d4")
        self.log_text.tag_configure("player", foreground="#9de2ff")
        self.log_text.tag_configure("enemy", foreground="#ff8f8f")
        self.log_text.tag_configure("heal", foreground="#9dffb3")
        self.log_text.tag_configure("warn", foreground="#ffd67a")
        self.log_text.tag_configure("success", foreground="#9dff7d")
        self.log_text.tag_configure("death", foreground="#ff4d4d")

    def _bind_shortcuts(self):
        self.bind("1", lambda _event: self._on_attack())
        self.bind("2", lambda _event: self._on_use_selected_item())
        self.bind("3", lambda _event: self._on_escape())
        self.bind("<n>", lambda _event: self._advance_room())
        self.bind("<N>", lambda _event: self._advance_room())
        self.bind("<Key>", self._on_secret_keypress)

    def _on_secret_keypress(self, event):
        if not event.char:
            return

        self._secret_input_buffer = (self._secret_input_buffer + event.char.lower())[-12:]
        if self._secret_input_buffer.endswith(self._secret_code):
            self._secret_input_buffer = ""
            self._open_enemy_lab()

    def _refresh_all(self):
        self._refresh_status()
        self._refresh_inventory()
        self._draw_player_bars()
        self._draw_scene()

    def _on_scene_configure(self, _event):
        # Debounce resize redraw to avoid noisy intermediate renders.
        if self._resize_after_id is not None:
            self.after_cancel(self._resize_after_id)
        self._resize_after_id = self.after(16, self._draw_scene)

    def _refresh_status(self):
        weapon = self.player.playerClass.equipedWeapon
        self.status_label.config(
            text=(
                f"Jogador: {self.player.name}\n"
                f"Papel: {getattr(self.player, 'hero_role', 'Operative')}\n"
                f"HP: {self.player.playerClass.healthPoints}/{self.player.playerClass.maxHealthPoints}\n"
                f"SP: {self.player.playerClass.sP}/{self.player.playerClass.maxSP}\n"
                f"XP: {self.player.xpPoints}\n"
                f"Arma: {weapon.weaponName} ({weapon.weaponRarity})\n"
                f"Dano total: {weapon.totaldmgValue + self.player.playerClass.baseAttack:.1f}\n"
                f"\n"
                f"Inimigo: {self.current_enemy.name}\n"
                f"HP inimigo: {max(0, self.current_enemy.healthPoints)}/{self.current_enemy.maxHealthPoints}\n"
                f"ATK inimigo: {self.current_enemy.attackDmg}"
            )
        )

    def _refresh_inventory(self):
        self.inventory_listbox.delete(0, tk.END)
        self.inventory_slot_map = []

        for slot_index, slot in list_player_consumables(self.player):
            self.inventory_slot_map.append(slot_index)
            self.inventory_listbox.insert(
                tk.END,
                f"{slot.consumable.name} x{slot.quantity} - {slot.consumable.description}",
            )

        if not self.inventory_slot_map:
            self.inventory_listbox.insert(tk.END, "(vazio)")
            self.use_item_button.config(state="disabled")
        else:
            self.use_item_button.config(state="normal")

    def _draw_player_bars(self):
        canvas = self.vitals_canvas
        canvas.delete("all")

        width = canvas.winfo_width()
        if width <= 1:
            width = 320
        height = canvas.winfo_height() or 84

        hp_ratio = self.player.playerClass.healthPoints / self.player.playerClass.maxHealthPoints
        sp_ratio = self.player.playerClass.sP / self.player.playerClass.maxSP
        hp_ratio = min(1.0, max(0.0, hp_ratio))
        sp_ratio = min(1.0, max(0.0, sp_ratio))

        canvas.create_text(12, 14, text="HP", fill="#ff9c9c", anchor="w", font=("Consolas", 10, "bold"))
        canvas.create_rectangle(48, 6, width - 10, 24, fill="#2e0a0a", outline="#5d1616")
        canvas.create_rectangle(48, 6, 48 + int((width - 58) * hp_ratio), 24, fill="#d12626", outline="")
        canvas.create_text(width - 14, 14, text=f"{self.player.playerClass.healthPoints}/{self.player.playerClass.maxHealthPoints}", fill="#ffd8d8", anchor="e", font=("Consolas", 9))

        canvas.create_text(12, 46, text="SP", fill="#9cd7ff", anchor="w", font=("Consolas", 10, "bold"))
        canvas.create_rectangle(48, 38, width - 10, 56, fill="#0a142e", outline="#19335d")
        canvas.create_rectangle(48, 38, 48 + int((width - 58) * sp_ratio), 56, fill="#2b93ff", outline="")
        canvas.create_text(width - 14, 46, text=f"{self.player.playerClass.sP}/{self.player.playerClass.maxSP}", fill="#cde9ff", anchor="e", font=("Consolas", 9))

        canvas.create_text(12, height - 10, text="Atalhos: 1=Atacar  2=Item  3=Fugir  N=Prox. Sala", fill="#8f8f8f", anchor="w", font=("Consolas", 8))

    def _open_enemy_lab(self):
        if self._enemy_lab_window is not None and self._enemy_lab_window.winfo_exists():
            self._enemy_lab_window.lift()
            self._enemy_lab_window.focus_force()
            return

        window = tk.Toplevel(self)
        window.title("Enemy Lab (Easter Egg)")
        window.geometry("460x420")
        window.configure(bg="#111111")
        window.resizable(False, False)
        self._enemy_lab_window = window

        stage_var = tk.IntVar(value=max(1, self.enemy_index + 1))
        boss_var = tk.BooleanVar(value=False)
        preview_var = tk.StringVar(value="Clique em GERAR para criar um inimigo.")
        preview_state = {"enemy": None}
        template_by_option = {f"{template.id} | {template.name}": template for template in ENEMY_TEMPLATES}
        model_var = tk.StringVar(value=next(iter(template_by_option.keys())))

        frame = tk.Frame(window, bg="#111111")
        frame.pack(fill="both", expand=True, padx=12, pady=12)

        tk.Label(frame, text="ENEMY LAB", bg="#111111", fg="#ff5a5a", font=("Consolas", 16, "bold")).pack(anchor="w")
        tk.Label(frame, text="Easter egg desbloqueado via IDDQD", bg="#111111", fg="#8f8f8f", font=("Consolas", 9)).pack(anchor="w", pady=(0, 10))

        controls = tk.Frame(frame, bg="#111111")
        controls.pack(fill="x")

        tk.Label(controls, text="Stage", bg="#111111", fg="#dcdcdc", font=("Consolas", 10)).grid(row=0, column=0, sticky="w")
        stage_spin = tk.Spinbox(controls, from_=1, to=99, textvariable=stage_var, width=6, font=("Consolas", 10))
        stage_spin.grid(row=0, column=1, sticky="w", padx=(6, 12))

        boss_check = tk.Checkbutton(
            controls,
            text="Boss Sector",
            variable=boss_var,
            bg="#111111",
            fg="#dcdcdc",
            selectcolor="#222222",
            activebackground="#111111",
            activeforeground="#ffffff",
            font=("Consolas", 10),
        )
        boss_check.grid(row=0, column=2, sticky="w")

        tk.Label(controls, text="Modelo", bg="#111111", fg="#dcdcdc", font=("Consolas", 10)).grid(row=1, column=0, sticky="w", pady=(8, 0))
        model_menu = tk.OptionMenu(controls, model_var, *template_by_option.keys())
        model_menu.config(bg="#222222", fg="#ffffff", activebackground="#333333", activeforeground="#ffffff", relief="flat", font=("Consolas", 9))
        model_menu["menu"].config(bg="#222222", fg="#ffffff", activebackground="#7e1313", activeforeground="#ffffff", font=("Consolas", 9))
        model_menu.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(6, 0), pady=(8, 0))

        preview_label = tk.Label(
            frame,
            textvariable=preview_var,
            justify="left",
            anchor="w",
            bg="#141414",
            fg="#f2f2f2",
            font=("Consolas", 10),
            padx=10,
            pady=10,
            relief="flat",
        )
        preview_label.pack(fill="x", pady=(10, 10))

        def generate_preview():
            stage = max(1, int(stage_var.get()))
            enemy = self.enemy_generator.generate_sector_enemy(stage, is_boss_sector=boss_var.get())
            preview_state["enemy"] = enemy
            _update_preview_text(enemy, source="RNG")

        def generate_from_model():
            selected = template_by_option[model_var.get()]
            enemy = self.enemy_generator.create_enemy_from_template(selected)
            preview_state["enemy"] = enemy
            _update_preview_text(enemy, source=f"MODEL {selected.id}")

        def _update_preview_text(enemy, source="RNG"):
            preview_var.set(
                f"Name: {enemy.name}\n"
                f"HP: {enemy.maxHealthPoints}  ATK: {enemy.attackDmg}  ARM: {enemy.armor}\n"
                f"XP: {enemy.xpReward}\n"
                f"Sprite: {getattr(enemy, 'sprite_key', enemy.name.lower())}\n"
                f"Template: {getattr(enemy, 'template_id', 'n/a')}\n"
                f"Source: {source}"
            )

        def edit_selected_model_sprite():
            selected = template_by_option[model_var.get()]
            suggested_key = f"{selected.sprite_key}_variant"
            self._open_sprite_editor(base_sprite_key=selected.sprite_key, suggested_key=suggested_key)

        def spawn_current_sector():
            if preview_state["enemy"] is None:
                generate_preview()
            enemy = copy.deepcopy(preview_state["enemy"])
            self.current_enemy = enemy
            self.enemies[self.enemy_index] = enemy
            self.attack_button.config(state="normal")
            self.escape_button.config(state="normal")
            self.next_button.config(state="disabled")
            self._floating_texts.clear()
            self._enemy_flash_ticks = 0
            self._log(f"Enemy Lab: {enemy.name} injetado no setor atual.", event_type="warn")
            self._refresh_all()

        def insert_next_sector():
            if preview_state["enemy"] is None:
                generate_preview()
            enemy = copy.deepcopy(preview_state["enemy"])
            self.enemies.insert(self.enemy_index + 1, enemy)
            self._log(f"Enemy Lab: {enemy.name} adicionado ao proximo setor.", event_type="warn")
            self._refresh_all()

        action_row = tk.Frame(frame, bg="#111111")
        action_row.pack(fill="x", pady=(0, 8))

        tk.Button(action_row, text="GERAR RNG", command=generate_preview, bg="#2a2a2a", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=(0, 4))
        tk.Button(action_row, text="GERAR MODELO", command=generate_from_model, bg="#4a4a4a", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=4)
        tk.Button(action_row, text="USAR AGORA", command=spawn_current_sector, bg="#7e1313", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=(4, 0))

        action_row_2 = tk.Frame(frame, bg="#111111")
        action_row_2.pack(fill="x", pady=(0, 8))
        tk.Button(action_row_2, text="INSERIR NEXT", command=insert_next_sector, bg="#1f4e21", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=(0, 4))
        tk.Button(action_row_2, text="EDITAR SPRITE DO MODELO", command=edit_selected_model_sprite, bg="#875f0f", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=4)
        tk.Button(action_row_2, text="ABRIR SPRITE EDITOR", command=self._open_sprite_editor, bg="#704b0b", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).pack(side="left", fill="x", expand=True, padx=(4, 0))

        generate_preview()

        def on_close():
            self._enemy_lab_window = None
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_close)

    def _open_sprite_editor(self, base_sprite_key=None, suggested_key=None):
        if self._sprite_editor_window is not None and self._sprite_editor_window.winfo_exists():
            self._sprite_editor_window.lift()
            self._sprite_editor_window.focus_force()
            if suggested_key:
                self._log(f"Sprite Editor ja aberto. Use key sugerida: {suggested_key}", event_type="info")
            return

        window = tk.Toplevel(self)
        window.title("Sprite Prototyper")
        window.geometry("760x620")
        window.configure(bg="#111111")
        self._sprite_editor_window = window

        rows = 10
        cols = 10
        cell = 24
        token_var = tk.StringVar(value="B")
        default_key = suggested_key if suggested_key else "prototype_enemy"
        key_var = tk.StringVar(value=default_key)
        grid_data = [["." for _ in range(cols)] for _ in range(rows)]
        palette_tokens = {
            "B": "#7a7572",
            "E": "#ff2c2c",
            "H": "#b7b2ad",
            "M": "#4a0f0f",
            ".": "#101010",
        }

        if base_sprite_key:
            if base_sprite_key in self._runtime_sprite_catalog:
                sprite = self._runtime_sprite_catalog[base_sprite_key]
                pattern, palette = sprite["pattern"], sprite["palette"]
            else:
                pattern, palette = get_enemy_sprite_data(base_sprite_key)

            for token in ["B", "E", "H", "M"]:
                if token in palette:
                    palette_tokens[token] = palette[token]

            for r in range(min(rows, len(pattern))):
                row_text = pattern[r]
                for c in range(min(cols, len(row_text))):
                    token = row_text[c]
                    grid_data[r][c] = token if token in ["B", "E", "H", "M", "."] else "."

        outer = tk.Frame(window, bg="#111111")
        outer.pack(fill="both", expand=True, padx=10, pady=10)
        outer.grid_columnconfigure(1, weight=1)
        outer.grid_rowconfigure(0, weight=1)

        left = tk.Frame(outer, bg="#111111")
        left.grid(row=0, column=0, sticky="nsw")

        tk.Label(left, text="Sprite Key", bg="#111111", fg="#dcdcdc", font=("Consolas", 10)).pack(anchor="w")
        tk.Entry(left, textvariable=key_var, font=("Consolas", 10), width=18).pack(anchor="w", pady=(0, 8))
        tk.Label(left, text="Token", bg="#111111", fg="#dcdcdc", font=("Consolas", 10)).pack(anchor="w")

        for token in ["B", "E", "H", "M", "."]:
            tk.Radiobutton(
                left,
                text=f"{token} ({'erase' if token == '.' else 'paint'})",
                variable=token_var,
                value=token,
                bg="#111111",
                fg="#f0f0f0",
                selectcolor="#222222",
                activebackground="#111111",
                activeforeground="#ffffff",
                font=("Consolas", 10),
            ).pack(anchor="w")

        canvas = tk.Canvas(left, width=cols * cell, height=rows * cell, bg="#0a0a0a", highlightthickness=1, highlightbackground="#3a3a3a")
        canvas.pack(anchor="w", pady=(12, 6))

        right = tk.Frame(outer, bg="#111111")
        right.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(1, weight=1)

        tk.Label(right, text="Preview Pattern", bg="#111111", fg="#ffce6a", font=("Consolas", 11, "bold")).grid(row=0, column=0, sticky="w")

        preview = tk.Text(right, bg="#0d0d0d", fg="#e6e6e6", insertbackground="#e6e6e6", relief="flat", font=("Consolas", 10), wrap="none")
        preview.grid(row=1, column=0, sticky="nsew", pady=(6, 8))

        button_row = tk.Frame(right, bg="#111111")
        button_row.grid(row=2, column=0, sticky="ew")
        button_row.grid_columnconfigure(0, weight=1)
        button_row.grid_columnconfigure(1, weight=1)
        button_row.grid_columnconfigure(2, weight=1)

        def render_grid():
            canvas.delete("all")
            for r in range(rows):
                for c in range(cols):
                    token = grid_data[r][c]
                    x0 = c * cell
                    y0 = r * cell
                    canvas.create_rectangle(
                        x0,
                        y0,
                        x0 + cell,
                        y0 + cell,
                        fill=palette_tokens.get(token, "#101010"),
                        outline="#1f1f1f",
                    )

        def build_pattern_lines():
            lines = []
            for row in grid_data:
                lines.append("".join(row).rstrip("."))
            cleaned = [line if line else "." for line in lines]
            return cleaned

        def refresh_preview():
            lines = build_pattern_lines()
            preview.config(state="normal")
            preview.delete("1.0", tk.END)
            preview.insert(tk.END, "pattern = [\n")
            for line in lines:
                preview.insert(tk.END, f"    \"{line}\",\n")
            preview.insert(tk.END, "]\n\n")
            preview.insert(tk.END, "palette = {\n")
            preview.insert(tk.END, "    \"B\": \"#7a7572\",\n")
            preview.insert(tk.END, "    \"E\": \"#ff2c2c\",\n")
            preview.insert(tk.END, "    \"H\": \"#b7b2ad\",\n")
            preview.insert(tk.END, "    \"M\": \"#4a0f0f\",\n")
            preview.insert(tk.END, "}\n")
            preview.config(state="disabled")

        def canvas_click(event):
            c = event.x // cell
            r = event.y // cell
            if 0 <= r < rows and 0 <= c < cols:
                grid_data[r][c] = token_var.get()
                render_grid()
                refresh_preview()

        def clear_grid():
            for r in range(rows):
                for c in range(cols):
                    grid_data[r][c] = "."
            render_grid()
            refresh_preview()

        def copy_pattern_to_clipboard():
            lines = build_pattern_lines()
            payload = "[\n" + "\n".join([f"    \"{line}\"," for line in lines]) + "\n]"
            self.clipboard_clear()
            self.clipboard_append(payload)
            self._log("Sprite Editor: pattern copiado para clipboard.", event_type="info")

        def copy_catalog_block():
            key = key_var.get().strip() or "prototype_enemy"
            lines = build_pattern_lines()
            block = (
                f"\"{key}\": {{\n"
                f"    \"pattern\": [\n" + "\n".join([f"        \"{line}\"," for line in lines]) +
                "\n    ],\n"
                "    \"palette\": {\n"
                "        \"B\": \"#7a7572\",\n"
                "        \"E\": \"#ff2c2c\",\n"
                "        \"H\": \"#b7b2ad\",\n"
                "        \"M\": \"#4a0f0f\",\n"
                "    },\n"
                "},"
            )
            self.clipboard_clear()
            self.clipboard_append(block)
            self._log("Sprite Editor: bloco de catalogo copiado.", event_type="info")

        def apply_runtime_sprite():
            key = key_var.get().strip() or "prototype_enemy"
            lines = build_pattern_lines()
            self._runtime_sprite_catalog[key] = {
                "pattern": lines,
                "palette": {
                    "B": "#7a7572",
                    "E": "#ff2c2c",
                    "H": "#b7b2ad",
                    "M": "#4a0f0f",
                },
            }
            self.current_enemy.sprite_key = key
            self._log(f"Sprite Editor: sprite runtime '{key}' aplicado ao inimigo atual.", event_type="success")
            self._refresh_all()

        canvas.bind("<Button-1>", canvas_click)

        tk.Button(button_row, text="LIMPAR", command=clear_grid, bg="#2a2a2a", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        tk.Button(button_row, text="COPIAR PATTERN", command=copy_pattern_to_clipboard, bg="#3c3c3c", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).grid(row=0, column=1, sticky="ew", padx=4)
        tk.Button(button_row, text="COPIAR BLOCO", command=copy_catalog_block, bg="#4a4a4a", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).grid(row=0, column=2, sticky="ew", padx=(4, 0))
        tk.Button(right, text="APLICAR NO INIMIGO ATUAL", command=apply_runtime_sprite, bg="#875f0f", fg="#ffffff", relief="flat", font=("Consolas", 10, "bold")).grid(row=3, column=0, sticky="ew", pady=(8, 0))

        render_grid()
        refresh_preview()

        def on_close():
            self._sprite_editor_window = None
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_close)

    def _draw_enemy_sprite(self, sector_left, sector_top, sector_right, sector_bottom):
        sprite_key = getattr(self.current_enemy, "sprite_key", self.current_enemy.name.lower())
        if sprite_key in self._runtime_sprite_catalog:
            sprite = self._runtime_sprite_catalog[sprite_key]
            pattern, palette = sprite["pattern"], sprite["palette"]
        else:
            pattern, palette = get_enemy_sprite_data(sprite_key)
        rows = len(pattern)
        cols = len(pattern[0])

        sector_width = sector_right - sector_left
        sector_height = sector_bottom - sector_top

        max_pixel_by_width = max(3, (sector_width - 80) // cols)
        max_pixel_by_height = max(3, (sector_height - 120) // rows)
        pixel = min(max_pixel_by_width, max_pixel_by_height, 22)
        pixel = max(6, pixel)

        sprite_width = cols * pixel
        sprite_height = rows * pixel

        desired_x = (sector_left + sector_right) // 2 - sprite_width // 2
        desired_y = sector_top + int(sector_height * 0.34)

        # Clamp sprite inside the visible sector area.
        x0 = max(sector_left + 10, min(desired_x, sector_right - sprite_width - 10))
        y0 = max(sector_top + 20, min(desired_y, sector_bottom - sprite_height - 52))

        self.scene_canvas.create_oval(
            x0 - 10,
            y0 + sprite_height - 6,
            x0 + sprite_width + 10,
            y0 + sprite_height + 24,
            fill="#160606",
            outline="",
        )

        for row_index, row_data in enumerate(pattern):
            for col_index, token in enumerate(row_data):
                if token == ".":
                    continue
                color = palette.get(token, "#ffffff")
                px = x0 + col_index * pixel
                py = y0 + row_index * pixel
                self.scene_canvas.create_rectangle(
                    px,
                    py,
                    px + pixel,
                    py + pixel,
                    fill=color,
                    outline="#0c0c0c",
                )

        self.scene_canvas.create_text(
            x0 + sprite_width // 2,
            y0 + sprite_height + 34,
            text=self.current_enemy.name.upper(),
            fill="#ffe6e6",
            font=("Consolas", 14, "bold"),
        )

        self._enemy_anchor = (x0 + sprite_width // 2, y0 + 8)

    def _draw_floating_numbers(self):
        for effect in self._floating_texts:
            self.scene_canvas.create_text(
                effect["x"],
                effect["y"],
                text=effect["text"],
                fill=effect["color"],
                font=("Consolas", 13, "bold"),
            )

    def _spawn_floating_number(self, text, target, color):
        if target == "enemy":
            x, y = self._enemy_anchor
        else:
            x, y = self._player_anchor

        self._floating_texts.append({
            "x": x,
            "y": y,
            "text": text,
            "color": color,
            "ttl": 26,
        })

    def _tick_effects(self):
        needs_redraw = False

        if self._enemy_flash_ticks > 0:
            self._enemy_flash_ticks -= 1
            needs_redraw = True

        next_effects = []
        for effect in self._floating_texts:
            effect["y"] -= 1.8
            effect["ttl"] -= 1
            if effect["ttl"] > 0:
                next_effects.append(effect)
                needs_redraw = True
        self._floating_texts = next_effects

        if needs_redraw:
            self._draw_scene()

        self.after(33, self._tick_effects)

    def _draw_scene(self):
        self._resize_after_id = None
        self.scene_canvas.delete("all")
        width = self.scene_canvas.winfo_width()
        height = self.scene_canvas.winfo_height()

        # Avoid drawing while the widget still has provisional tiny size.
        if width < 220 or height < 220:
            return

        # Retro corridor inspired by classic FPS tunnel perspective.
        for i in range(10):
            shade = 15 + i * 8
            color = f"#{shade:02x}{shade:02x}{shade:02x}"
            margin_x = i * 22
            margin_y = i * 16
            self.scene_canvas.create_rectangle(
                margin_x,
                margin_y,
                width - margin_x,
                height - margin_y,
                outline=color,
            )

        sector_left = 84
        sector_top = 70
        sector_right = width - 84
        sector_bottom = height - 82
        self.scene_canvas.create_rectangle(
            sector_left,
            sector_top,
            sector_right,
            sector_bottom,
            outline="#ff4d4d" if self._enemy_flash_ticks > 0 else "#7e1313",
            width=3 if self._enemy_flash_ticks > 0 else 2,
        )

        self.scene_canvas.create_text(
            width // 2,
            30,
            text=f"SECTOR {self.enemy_index + 1}/{len(self.enemies)}",
            fill="#ff5a5a",
            font=("Consolas", 18, "bold"),
        )

        self._draw_enemy_sprite(sector_left, sector_top, sector_right, sector_bottom)
        self._draw_floating_numbers()

        self._player_anchor = (width - 110, height - 76)

        enemy_hp_ratio = max(0.0, self.current_enemy.healthPoints / self.current_enemy.maxHealthPoints)
        self.scene_canvas.create_rectangle(30, height - 46, width - 30, height - 24, fill="#260606", outline="#521010")
        hp_bar_width = int((width - 60) * enemy_hp_ratio)
        self.scene_canvas.create_rectangle(30, height - 46, 30 + hp_bar_width, height - 24, fill="#d12626", outline="")

        # Hidden easter egg trigger button.
        self.scene_canvas.create_text(
            width - 10,
            height - 10,
            text=".",
            fill="#0c0c0c",
            activefill="#3a3a3a",
            tags="enemy_lab_trigger",
            font=("Consolas", 8),
        )
        self.scene_canvas.tag_bind("enemy_lab_trigger", "<Button-1>", lambda _event: self._open_enemy_lab())

    def _log(self, message, event_type="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n", event_type)
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def _enemy_turn(self):
        enemy_attack_damage, applied_enemy_damage = resolve_enemy_attack(self.player, self.current_enemy)
        self._spawn_floating_number(f"-{applied_enemy_damage}", target="player", color="#ff8f8f")
        self._log(
            f"{self.current_enemy.name} contra-ataca. Dano bruto: {enemy_attack_damage} | efetivo: {applied_enemy_damage}.",
            event_type="enemy",
        )
        if self.player.playerClass.healthPoints <= 0:
            self._log("Voce morreu. Execucao encerrada.", event_type="death")
            self._disable_actions()
            messagebox.showerror("Fim de jogo", "Voce foi derrotado.")

    def _on_attack(self):
        if self._combat_locked():
            return

        attack_damage, applied_player_damage = resolve_player_attack(self.player, self.current_enemy)
        self._enemy_flash_ticks = 5
        self._spawn_floating_number(f"-{applied_player_damage}", target="enemy", color="#ff5858")
        self._log(
            f"Voce atacou {self.current_enemy.name} com {self.player.playerClass.equipedWeapon.weaponName}. "
            f"Dano bruto: {attack_damage} | efetivo: {applied_player_damage}.",
            event_type="player",
        )

        if self.current_enemy.healthPoints <= 0:
            self._handle_enemy_defeat()
        else:
            self._enemy_turn()

        self._refresh_all()

    def _on_use_selected_item(self):
        if self._combat_locked():
            return

        selection = self.inventory_listbox.curselection()
        if not selection or not self.inventory_slot_map:
            self._log("Nenhum item selecionado.", event_type="warn")
            return

        slot_index = self.inventory_slot_map[selection[0]]
        success, message = use_player_consumable(self.player, slot_index)
        event_type = "heal" if success else "warn"
        self._log(message, event_type=event_type)
        if success and "HP" in message:
            self._spawn_floating_number("+HP", target="player", color="#9dffb3")
        if success and "SP" in message:
            self._spawn_floating_number("+SP", target="player", color="#8fd0ff")

        if success and self.current_enemy.healthPoints > 0:
            self._enemy_turn()

        self._refresh_all()

    def _on_escape(self):
        if self._combat_locked():
            return

        escaped = attempt_player_escape(self.player)
        if escaped:
            self._log("Fuga bem-sucedida. Avance para o proximo setor.", event_type="success")
            self.next_button.config(state="normal")
            self.attack_button.config(state="disabled")
            self.escape_button.config(state="disabled")
        else:
            self._log(f"Fuga falhou. {self.current_enemy.name} perdeu o ataque no caos do corredor.", event_type="warn")

        self._refresh_all()

    def _handle_enemy_defeat(self):
        self.player.xpPoints += self.current_enemy.xpReward
        self._log(f"{self.current_enemy.name} caiu. XP +{self.current_enemy.xpReward}.", event_type="success")

        if isinstance(self.current_enemy, Boss):
            boss_drop = self.current_enemy.drop_weapon()
            self.player.playerClass.equipedWeapon = boss_drop
            self._log(
                "Boss drop: "
                f"{boss_drop.weaponName} ({boss_drop.weaponRarity}) dano base {boss_drop.baseDamage}.",
                event_type="success",
            )

        self.next_button.config(state="normal")
        self.attack_button.config(state="disabled")
        self.escape_button.config(state="disabled")

    def _advance_room(self):
        if self.enemy_index + 1 >= len(self.enemies):
            self._log("Todos os setores limpos. Vitoria total.", event_type="success")
            self._disable_actions()
            messagebox.showinfo("Vitoria", "Todos os inimigos foram derrotados.")
            return

        self.enemy_index += 1
        self.current_enemy = self.enemies[self.enemy_index]
        self._floating_texts.clear()
        self._enemy_flash_ticks = 0
        self._log(f"Novo contato hostil detectado: {self.current_enemy.name}.", event_type="info")

        self.attack_button.config(state="normal")
        self.escape_button.config(state="normal")
        self.next_button.config(state="disabled")

        self._refresh_all()

    def _combat_locked(self):
        return str(self.attack_button["state"]) == "disabled" and str(self.next_button["state"]) == "disabled"

    def _disable_actions(self):
        self.attack_button.config(state="disabled")
        self.escape_button.config(state="disabled")
        self.next_button.config(state="disabled")


def run():
    app = DoomDungeonUI()
    app.mainloop()


if __name__ == "__main__":
    run()
