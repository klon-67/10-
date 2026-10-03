import tkinter as tk
import random


# ============================================================
# COOKIE CLICKER
# Легка гра-клікер на Python + Tkinter
# ============================================================


# ============================================================
# НАЛАШТУВАННЯ ГРИ
# ============================================================

coins = 0
total_coins = 0
click_power = 1
auto_power = 0

level = 1
clicks = 0
best_click = 0

game_running = True

upgrade_click_cost = 25
upgrade_auto_cost = 100
upgrade_level_cost = 500

achievements = []

cookie_size = 1


# ============================================================
# СТВОРЕННЯ ВІКНА
# ============================================================

root = tk.Tk()

root.title("🍪 Cookie Clicker")
root.geometry("700x750")
root.resizable(False, False)


# ============================================================
# ЗАГОЛОВОК
# ============================================================

title = tk.Label(
    root,
    text="🍪 COOKIE CLICKER 🍪",
    font=("Arial", 28, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Клікай на печиво та заробляй монетки!",
    font=("Arial", 13)
)

subtitle.pack()


# ============================================================
# ИНФОРМАЦІЯ
# ============================================================

info_frame = tk.Frame(root)

info_frame.pack(pady=15)


coins_label = tk.Label(
    info_frame,
    text="Монети: 0",
    font=("Arial", 16, "bold")
)

coins_label.grid(row=0, column=0, padx=20)


level_label = tk.Label(
    info_frame,
    text="Рівень: 1",
    font=("Arial", 16)
)

level_label.grid(row=0, column=1, padx=20)


clicks_label = tk.Label(
    info_frame,
    text="Кліків: 0",
    font=("Arial", 16)
)

clicks_label.grid(row=0, column=2, padx=20)


# ============================================================
# ПОВІДОМЛЕННЯ
# ============================================================

message_label = tk.Label(
    root,
    text="Натисни на печиво!",
    font=("Arial", 14)
)

message_label.pack(pady=10)


# ============================================================
# ПЕЧИВО
# ============================================================

cookie_button = tk.Button(
    root,
    text="🍪",
    font=("Arial", 90),
    width=4,
    height=2,
    relief="raised",
    bd=8
)

cookie_button.pack(pady=20)


# ============================================================
# ФУНКЦІЯ ОНОВЛЕННЯ ІНФОРМАЦІЇ
# ============================================================

def update_display():

    coins_label.config(
        text=f"Монети: {coins}"
    )

    level_label.config(
        text=f"Рівень: {level}"
    )

    clicks_label.config(
        text=f"Кліків: {clicks}"
    )

    click_upgrade_button.config(
        text=f"🖱️ Покращити клік\nЦіна: {upgrade_click_cost}"
    )

    auto_upgrade_button.config(
        text=f"⚙️ Автоклік\nЦіна: {upgrade_auto_cost}"
    )

    level_upgrade_button.config(
        text=f"⭐ Новий рівень\nЦіна: {upgrade_level_cost}"
    )


# ============================================================
# КЛІК ПО ПЕЧИВУ
# ============================================================

def click_cookie():

    global coins
    global total_coins
    global clicks
    global best_click
    global level

    bonus = random.randint(0, 3)

    earned = click_power + bonus

    coins += earned
    total_coins += earned

    clicks += 1

    if earned > best_click:
        best_click = earned

    # Кожні 50 кліків новий рівень
    new_level = clicks // 50 + 1

    if new_level > level:

        level = new_level

        message_label.config(
            text=f"🎉 Новий рівень! Тепер ти рівень {level}!"
        )

    else:

        message_label.config(
            text=f"+{earned} 🍪"
        )

    check_achievements()

    update_display()


# ============================================================
# ПОКРАЩЕННЯ КЛІКУ
# ============================================================

def upgrade_click():

    global coins
    global click_power
    global upgrade_click_cost

    if coins >= upgrade_click_cost:

        coins -= upgrade_click_cost

        click_power += 1

        upgrade_click_cost = int(
            upgrade_click_cost * 1.6
        )

        message_label.config(
            text=f"🖱️ Клік тепер дає +{click_power}!"
        )

        update_display()

    else:

        message_label.config(
            text="❌ Недостатньо монет!")


# ============================================================
# АВТОКЛІК
# ============================================================

def upgrade_auto():

    global coins
    global auto_power
    global upgrade_auto_cost

    if coins >= upgrade_auto_cost:

        coins -= upgrade_auto_cost

        auto_power += 1

        upgrade_auto_cost = int(
            upgrade_auto_cost * 1.8
        )

        message_label.config(
            text=f"⚙️ Автоклік: {auto_power}/сек"
        )

        update_display()

    else:

        message_label.config(
            text="❌ Недостатньо монет!"
        )


# ============================================================
# ПОКРАЩЕННЯ РІВНЯ
# ============================================================

def upgrade_level():

    global coins
    global level
    global upgrade_level_cost

    if coins >= upgrade_level_cost:

        coins -= upgrade_level_cost

        level += 1

        upgrade_level_cost = int(
            upgrade_level_cost * 2
        )

        message_label.config(
            text=f"⭐ Ти досяг рівня {level}!"
        )

        update_display()

    else:

        message_label.config(
            text="❌ Потрібно більше монет!"
        )


# ============================================================
# АВТОМАТИЧНИЙ ДОХІД
# ============================================================

def auto_click():

    global coins
    global total_coins

    if auto_power > 0:

        coins += auto_power

        total_coins += auto_power

        check_achievements()

        update_display()

    root.after(1000, auto_click)


# ============================================================
# ДОСЯГНЕННЯ
# ============================================================

def check_achievements():

    global achievements

    if clicks >= 10 and "10 кліків" not in achievements:

        achievements.append("10 кліків")

        message_label.config(
            text="🏆 Досягнення: 10 кліків!"
        )

    if clicks >= 100 and "100 кліків" not in achievements:

        achievements.append("100 кліків")

        message_label.config(
            text="🏆 Досягнення: 100 кліків!"
        )

    if total_coins >= 1000 and "1000 монет" not in achievements:

        achievements.append("1000 монет")

        message_label.config(
            text="🏆 Досягнення: 1000 монет!"
        )

    if level >= 10 and "Рівень 10" not in achievements:

        achievements.append("Рівень 10")

        message_label.config(
            text="🏆 Досягнення: Рівень 10!"
        )


# ============================================================
# ВІКНО ДОСЯГНЕНЬ
# ============================================================

def show_achievements():

    window = tk.Toplevel(root)

    window.title("🏆 Досягнення")

    window.geometry("400x400")

    title2 = tk.Label(
        window,
        text="🏆 Твої досягнення",
        font=("Arial", 20, "bold")
    )

    title2.pack(pady=20)

    if len(achievements) == 0:

        label = tk.Label(
            window,
            text="Поки що немає досягнень 😢",
            font=("Arial", 14)
        )

        label.pack(pady=20)

    else:

        for achievement in achievements:

            label = tk.Label(
                window,
                text=f"🏆 {achievement}",
                font=("Arial", 14)
            )

            label.pack(pady=5)


# ============================================================
# СТАТИСТИКА
# ============================================================

def show_stats():

    window = tk.Toplevel(root)

    window.title("📊 Статистика")

    window.geometry("400x400")

    title2 = tk.Label(
        window,
        text="📊 Статистика",
        font=("Arial", 22, "bold")
    )

    title2.pack(pady=20)

    stats = [
        f"🍪 Всього монет: {total_coins}",
        f"🖱️ Всього кліків: {clicks}",
        f"⭐ Рівень: {level}",
        f"💪 Сила кліку: {click_power}",
        f"⚙️ Автоклік: {auto_power}/сек",
        f"🏆 Досягнень: {len(achievements)}",
        f"🔥 Найкращий клік: {best_click}"
    ]

    for text in stats:

        label = tk.Label(
            window,
            text=text,
            font=("Arial", 14)
        )

        label.pack(pady=7)


# ============================================================
# ВИПАДКОВИЙ БОНУС
# ============================================================

def random_bonus():

    global coins

    if random.randint(1, 20) == 1:

        bonus = random.randint(10, 50)

        coins += bonus

        message_label.config(
            text=f"🎁 БОНУС! +{bonus} монет!"
        )

        update_display()

    root.after(5000, random_bonus)


# ============================================================
# КРИТИЧНИЙ КЛІК
# ============================================================

def critical_click(event):

    global coins
    global total_coins

    if random.randint(1, 15) == 1:

        bonus = click_power * 5

        coins += bonus
        total_coins += bonus

        message_label.config(
            text=f"🔥 КРИТИЧНИЙ КЛІК! +{bonus}!"
        )

        update_display()


# ============================================================
# СКИДАННЯ ГРИ
# ============================================================

def reset_game():

    global coins
    global total_coins
    global click_power
    global auto_power
    global level
    global clicks
    global best_click
    global upgrade_click_cost
    global upgrade_auto_cost
    global upgrade_level_cost
    global achievements

    coins = 0
    total_coins = 0

    click_power = 1
    auto_power = 0

    level = 1
    clicks = 0
    best_click = 0

    upgrade_click_cost = 25
    upgrade_auto_cost = 100
    upgrade_level_cost = 500

    achievements = []

    message_label.config(
        text="🔄 Гра була скинута!"
    )

    update_display()


# ============================================================
# МЕНЮ ПОКРАЩЕНЬ
# ============================================================

upgrade_frame = tk.LabelFrame(
    root,
    text="🛒 Магазин",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=10
)

upgrade_frame.pack(
    pady=10,
    padx=20,
    fill="x"
)


# ============================================================
# КНОПКА ПОКРАЩЕННЯ КЛІКУ
# ============================================================

click_upgrade_button = tk.Button(
    upgrade_frame,
    text="🖱️ Покращити клік",
    font=("Arial", 12),
    width=25,
    height=2,
    command=upgrade_click
)

click_upgrade_button.pack(
    pady=5
)


# ============================================================
# КНОПКА АВТОКЛІКУ
# ============================================================

auto_upgrade_button = tk.Button(
    upgrade_frame,
    text="⚙️ Купити автоклік",
    font=("Arial", 12),
    width=25,
    height=2,
    command=upgrade_auto
)

auto_upgrade_button.pack(
    pady=5
)


# ============================================================
# КНОПКА РІВНЯ
# ============================================================

level_upgrade_button = tk.Button(
    upgrade_frame,
    text="⭐ Підвищити рівень",
    font=("Arial", 12),
    width=25,
    height=2,
    command=upgrade_level
)

level_upgrade_button.pack(
    pady=5
)


# ============================================================
# ДОДАТКОВЕ МЕНЮ
# ============================================================

menu_frame = tk.Frame(root)

menu_frame.pack(pady=10)


achievements_button = tk.Button(
    menu_frame,
    text="🏆 Досягнення",
    font=("Arial", 11),
    width=15,
    command=show_achievements
)

achievements_button.grid(
    row=0,
    column=0,
    padx=5
)


stats_button = tk.Button(
    menu_frame,
    text="📊 Статистика",
    font=("Arial", 11),
    width=15,
    command=show_stats
)

stats_button.grid(
    row=0,
    column=1,
    padx=5
)


reset_button = tk.Button(
    menu_frame,
    text="🔄 Скинути",
    font=("Arial", 11),
    width=15,
    command=reset_game
)

reset_button.grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# ПІДКАЗКА
# ============================================================

hint_label = tk.Label(
    root,
    text="💡 Порада: купуй автокліки, щоб заробляти монети автоматично!",
    font=("Arial", 10)
)

hint_label.pack(
    pady=10
)


# ============================================================
# ПОДІЯ КЛІКУ
# ============================================================

cookie_button.config(
    command=click_cookie
)


cookie_button.bind(
    "<Button-1>",
    critical_click
)


# ============================================================
# ПЕРШЕ ОНОВЛЕННЯ
# ============================================================

update_display()


# ============================================================
# ЗАПУСК АВТОКЛІКУ
# ============================================================

root.after(
    1000,
    auto_click
)


# ============================================================
# ВИПАДКОВІ БОНУСИ
# ============================================================

root.after(
    5000,
    random_bonus
)


# ============================================================
# ЗАПУСК ПРОГРАМИ
# ============================================================

root.mainloop()
