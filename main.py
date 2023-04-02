import tkinter as tk
from PIL import Image, ImageTk

PICSIZE = (860, 540)
window = tk.Tk()
window.geometry('860x540')

flag_church = 0
flag_school = 0
flag_magik = 0
flag_knife = 0
flag_teacher = 0
flag_mimik = 0
flag_good_magik = 0
x = 0

canvas = tk.Canvas(window, height=540, width=860)
image = Image.open('Начало.png')
image = image.resize(PICSIZE)
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.pack()


def kill():
    window.destroy()


def kill_but():
    global flag_church, flag_school, flag_magik, flag_knife, x, flag_teacher, photo
    but1.place_forget()
    image = Image.open('Смерть.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    but2['text'] = 'Начать заново'
    but2['command'] = forest
    but3.place_forget()
    starter['text'] = 'Завершить игру'
    starter['command'] = kill
    starter.place(relx=0.5, rely=0.5)
    but2.place(relx=0.4, rely=0.8)
    flag_church = 0
    flag_school = 0
    flag_magik = 0
    flag_knife = 0
    flag_teacher = 0
    flag_mimik = 0
    flag_good_magik = 0
    x = 0


def victory():
    global photo
    kill_but()
    image = Image.open('Победа.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)


def church():
    global photo, flag_church, flag_school
    flag_church = 1

    def death1():  # Зажал денег, священник покарал
        global photo

        def death():
            global photo
            image = Image.open('БабкаСмерть2.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but2['text'] = 'Далее'
            but2['command'] = kill_but

        image = Image.open('БабкаСмерть.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = death
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()

    def death2():  # На вопрос священника не ответил
        global photo
        image = Image.open('СвященникСмерть.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        but4.place_forget()
        but5.place_forget()
        but6.place_forget()

    def pop():
        global photo

        def pop_village():
            global photo
            village()
            image = Image.open('Деревня.jpg')  # пустая деревня
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but2.place_forget()
            if flag_school == 1:
                but3.place_forget()
            but4.place_forget()
            but5.place_forget()
            but6.place_forget()

        def pop_question():
            global photo
            image = Image.open('СвященникВопрос.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Космос'
            but1['command'] = death2
            but2['text'] = 'Симфония'
            but2['command'] = death2
            but2.place(relx=0.4, rely=0.8)
            but3['text'] = 'Вопли'
            but3['command'] = death2
            but4['command'] = pop_village
            but4.place(relx=0.7, rely=0.6)
            but5['command'] = death2
            but5.place(relx=0.4, rely=0.6)
            but6['command'] = death2
            but6.place(relx=0.1, rely=0.6)

        image = Image.open('Священник.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1['text'] = 'Отвечать'
        but1['command'] = pop_question
        but2.place_forget()
        but3['text'] = 'Убежать'
        but3['command'] = pop_village

    def victory_church():
        global photo
        kill_but()
        image = Image.open('Алтарь.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def babka():
        global photo

        def sovet_babka():
            global photo
            church_babka()
            image = Image.open('СоветБабка.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)

        def church_babka():
            global photo
            church()
            image = Image.open('Церковь.jpg')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but2.place_forget()

        image = Image.open('Бабка.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1['text'] = '10'
        but1['command'] = death1
        but2['text'] = '50'
        but2['command'] = church_babka
        but3['text'] = '100'
        but3['command'] = sovet_babka

    image = Image.open('Церковь.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    but1['text'] = 'Подойти к алтарю'
    but1['command'] = victory_church
    but1.place(relx=0.7, rely=0.8)
    but2['text'] = 'Подать милостыню'
    but2['command'] = babka
    but2.place(relx=0.4, rely=0.8)
    but3['text'] = 'Подняться по лестнице'
    but3['command'] = pop
    but3.place(relx=0.1, rely=0.8)


def home():
    global photo

    def death1():  # Подскользнулся и умер
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('1.jpg')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death2():  # Дом сожрал
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('1.jpg')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death3():  # Затащили в ад
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('ЛюкСмерть.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death4():  # Собака тебя сжирака
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('ЗаднийДворТварюшка.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death5():  # Свалились в могилу
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('ЗаднийДворМогила.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def podval():
        global photo
        image = Image.open('Подвал.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

        def to_church():
            global photo
            image = Image.open('ЛюкЦерковь.png')  # вас перенесло в церковь
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but2['command'] = church
            but2['text'] = 'Далее'
            but1.place_forget()
            but3.place_forget()

        def luk():
            global photo
            image = Image.open('Люк.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Гнев'
            but1['command'] = death2
            but2['text'] = 'Чревоугодие'
            but2['command'] = death3
            but3['text'] = 'Уныние'
            but3['command'] = to_church  # Крипта в церковь

        def to_church_morda():
            global photo
            image = Image.open('МордаЦерковь.png')  # вас перенесло в церковь
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but2['command'] = church
            but2['text'] = 'Далее'
            but1.place_forget()
            but3.place_forget()

        but1['text'] = 'Железная дева'
        but1['command'] = death1
        but2['text'] = 'Люк'
        but2['command'] = luk  # Выбор смерти
        but2.place(relx=0.4, rely=0.8)
        but3['text'] = 'Морда на стене'
        but3['command'] = to_church_morda

    def garden():
        global photo
        image = Image.open('ЗаднийДвор.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1['text'] = 'Осмотреть территорию'  # Собака тебя сжирака
        but1['command'] = death4
        but2['text'] = 'Подойти к склепу'  # Победа
        but2['command'] = victory
        but2.place(relx=0.4, rely=0.8)
        but3['text'] = 'Подойти к могильной плите'  # Затащили в могилу
        but3['command'] = death5

    image = Image.open('Домик.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    but1['text'] = 'Выйти на задний двор'
    but1['command'] = garden
    but1.place(relx=0.7, rely=0.8)
    but2.place_forget()
    but3['text'] = 'Спуститься в подвал'
    but3['command'] = podval
    but3.place(relx=0.1, rely=0.8)


def village():
    global photo

    def death1():  # Встретил мимика
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('СундукВперед.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death1_2():  # Ушел от мимика
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('МимикНазад.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def death2():  # Не ответил училке
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('УчилкаСмерть.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def magik():
        global photo, flag_magik
        flag_magik = 1

        def vay_victory():
            global photo
            but1.place_forget()
            but2['text'] = 'Далее'
            but2['command'] = kill_but
            but2.place(relx=0.4, rely=0.8)
            but3.place_forget()
            image = Image.open('Победа.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)

        def good_magik():
            global photo, flag_good_magik
            flag_good_magik = 1

            def sovet_magik():
                global photo
                village()
                image = Image.open('ДобрыйКолдунСовет.png')  # магический совет
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)

            if flag_school == 1 and flag_church == 1:
                vay_victory()  # прошел все предыдущие локации в деревне
            image = Image.open('ДобрыйКолдунВопрос.png')  # вопрос по песне
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = "I am the stupid fool in the shed"  #
            but1['command'] = forest
            but1.place(relx=0.7, rely=0.8)
            but2['text'] = "I ain't the sharpest tool in the shed"  # выигрыш
            but2['command'] = sovet_magik
            but2.place(relx=0.4, rely=0.8)
            but3['text'] = "I'm not the sharpest tool in the shed"  #
            but3['command'] = forest
            but3.place(relx=0.1, rely=0.8)

        def bad_magik():
            global photo

            def no_knife_die():
                global photo

                def death1():
                    global photo
                    but1.place_forget()
                    but2['text'] = 'Далее'
                    but2['command'] = kill_but
                    but2.place(relx=0.4, rely=0.8)
                    but3.place_forget()
                    image = Image.open('ЗлойКолдунСмерть.png')  # нас убило
                    image = image.resize(PICSIZE)
                    photo = ImageTk.PhotoImage(image)
                    image = canvas.create_image(0, 0, anchor='nw', image=photo)

                image = Image.open('ЗлойКолдунНапал.png')
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)
                but1.place_forget()
                but2['text'] = 'Далее'
                but2['command'] = death1
                but2.place(relx=0.4, rely=0.8)
                but3.place_forget()

            def magik_knife():
                def magik_victory():
                    global photo
                    but1.place_forget()
                    but2['text'] = 'Далее'
                    but2['command'] = victory
                    but2.place(relx=0.4, rely=0.8)
                    but3.place_forget()
                    image = Image.open('ЗлойКолдунПобеда.png')
                    image = image.resize(PICSIZE)
                    photo = ImageTk.PhotoImage(image)
                    image = canvas.create_image(0, 0, anchor='nw', image=photo)

                global photo
                but1.place_forget()
                but2['text'] = 'Далее'
                but2['command'] = magik_victory
                but2.place(relx=0.4, rely=0.8)
                but3.place_forget()
                image = Image.open('ЗлойКолдунНапал.png')
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)

            image = Image.open('ЗлойКолдун.png')  # брать ли нож
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Не брать'
            but1['command'] = no_knife_die
            but1.place(relx=0.7, rely=0.8)
            but2.place_forget()
            but3['text'] = 'Взять'
            but3['command'] = magik_knife
            but3.place(relx=0.1, rely=0.8)

        image = Image.open('КолдунВыбор.png')  # философский вопрос
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1['text'] = 'Мудрость'
        but1['command'] = good_magik
        but1.place(relx=0.7, rely=0.8)
        but2.place_forget()
        but3['text'] = 'Разум'
        but3['command'] = bad_magik
        but3.place(relx=0.1, rely=0.8)

    def school():
        global flag_school, flag_church, photo, flag_teacher, flag_mimik
        flag_school = 1

        def teacher():
            global photo, flag_teacher
            flag_teacher = 1

            def teacher_question1():
                global photo

                def teacher_question2():
                    global photo

                    def teacher_school():
                        global photo
                        school()
                        image = Image.open('Школа.jpg')
                        image = image.resize(PICSIZE)
                        photo = ImageTk.PhotoImage(image)
                        image = canvas.create_image(0, 0, anchor='nw', image=photo)
                        but1.place_forget()

                    def teacher_village():
                        global photo
                        village()
                        image = Image.open('Деревня.jpg')
                        image = image.resize(PICSIZE)
                        photo = ImageTk.PhotoImage(image)
                        image = canvas.create_image(0, 0, anchor='nw', image=photo)
                        but3.place_forget()
                        if flag_church == 1:
                            but2.place_forget()

                    def teacher_question3():
                        global photo

                        def sovet_teacher():
                            global photo
                            image = Image.open('УчилкаСовет.png')  # совет: не стоит пренебрегать возможностями
                            image = image.resize(PICSIZE)
                            photo = ImageTk.PhotoImage(image)
                            image = canvas.create_image(0, 0, anchor='nw', image=photo)
                            but1.place_forget()
                            but3.place_forget()
                            but2['text'] = 'Далее'
                            but2['command'] = teacher_school

                        image = Image.open('Училка3.png')  # картинка с вопросом 3
                        image = image.resize(PICSIZE)
                        photo = ImageTk.PhotoImage(image)
                        image = canvas.create_image(0, 0, anchor='nw', image=photo)
                        but1['text'] = 'Меловом'  # верный ответ
                        but1['command'] = sovet_teacher
                        but2['text'] = 'Юрском'  # неверный ответ
                        but2['command'] = teacher_village
                        but2.place(relx=0.4, rely=0.8)
                        but3['text'] = 'Триасовом'  # неверный ответ
                        but3['command'] = teacher_village

                    image = Image.open('Училка2.png')  # картинка с вопросом 2
                    image = image.resize(PICSIZE)
                    photo = ImageTk.PhotoImage(image)
                    image = canvas.create_image(0, 0, anchor='nw', image=photo)
                    but1['text'] = '3-5'  # верный ответ
                    but1['command'] = teacher_question3
                    but2['text'] = '4-6'  # неверный ответ
                    but2['command'] = teacher_village
                    but2.place(relx=0.4, rely=0.8)
                    but3['text'] = '2-4'  # неверный ответ
                    but3['command'] = death2

                image = Image.open('Училка1.png')  # картинка с вопросом 1
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)
                but1['text'] = '23'  # верный ответ
                but1['command'] = teacher_question2
                but2['text'] = '46'  # неверный ответ
                but2['command'] = death2
                but2.place(relx=0.4, rely=0.8)
                but3['text'] = '38'  # неверный ответ
                but3['command'] = death2

            image = Image.open('УчилкаВступление.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Отвечать'
            but1['command'] = teacher_question1
            but2.place_forget()
            but3['text'] = 'Не отвечать'
            but3['command'] = death2

        def mimik():
            global photo, flag_mimik
            flag_mimik = 1

            def sovet_mimik():
                global photo, x
                x = 1

                def school_mimik():
                    school()
                    image = Image.open('Школа.jpg')
                    image = image.resize(PICSIZE)
                    photo = ImageTk.PhotoImage(image)
                    image = canvas.create_image(0, 0, anchor='nw', image=photo)
                    but2.place_forget()

                image = Image.open('БиблаСовет.png')
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)
                but1.place_forget()
                but3.place_forget()
                but2['text'] = 'Далее'
                but2['command'] = school_mimik

            image = Image.open('Библа.png')  # библа
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Открыть с цепью вперед'
            but1.place(relx=0.7, rely=0.8)
            but1['command'] = death1
            but2['text'] = 'Не открывать вообще'
            but2['command'] = death1_2
            but2.place(relx=0.4, rely=0.8)
            but3['text'] = 'Открыть с цепью назад'
            but3['command'] = sovet_mimik
            but3.place(relx=0.1, rely=0.8)

        def canteen():
            global photo

            def school_canteen():
                global photo
                school()
                image = Image.open('Школа.jpg')
                image = image.resize(PICSIZE)
                photo = ImageTk.PhotoImage(image)
                image = canvas.create_image(0, 0, anchor='nw', image=photo)
                if x == 1:
                    but2.place_forget()

            image = Image.open('Столовая.png')
            image = image.resize(PICSIZE)
            photo = ImageTk.PhotoImage(image)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            but1['text'] = 'Не брать рулет'
            but1['command'] = school_canteen
            but1.place(relx=0.7, rely=0.8)
            but2.place_forget()
            but3['text'] = 'Взять рулет'
            but3['command'] = victory
            but3.place(relx=0.1, rely=0.8)

        image = Image.open('Школа.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        but1['text'] = 'Пойти направо'
        but1['command'] = teacher
        but1.place(relx=0.7, rely=0.8)
        but2['text'] = 'Пойти прямо'
        but2['command'] = mimik
        but2.place(relx=0.4, rely=0.8)
        but3['text'] = 'Пойти налево'
        but3['command'] = canteen
        but3.place(relx=0.1, rely=0.8)
        if flag_teacher == 1:
            but1.place_forget()
        if flag_mimik == 1:
            but2.place_forget()

    image = Image.open('Поселение.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    but1['text'] = 'Подойти к дому'
    but1['command'] = magik
    but1.place(relx=0.7, rely=0.8)
    but2['text'] = 'Подойти к церкви'
    but2['command'] = church
    but2.place(relx=0.4, rely=0.8)
    but3['text'] = 'Подойти близжайшему строению'
    but3['command'] = school
    but3.place(relx=0.1, rely=0.8)
    if flag_magik == 1:
        but1.place_forget()


def polana():
    global photo

    def death1():  # Зверушка сожрала
        global photo
        but1.place_forget()
        but2['text'] = 'Далее'
        but2['command'] = kill_but
        but2.place(relx=0.4, rely=0.8)
        but3.place_forget()
        image = Image.open('СилуэтСмерть.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)

    def forest_back():
        global photo
        forest()
        image = Image.open('Лес.jpeg')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        starter.place_forget()
        but1['text'] = 'Пойти направо'
        but1['command'] = home
        but1.place(relx=0.7, rely=0.8)
        but2.place_forget()
        but3['text'] = 'Пойти налево'
        but3['command'] = village
        but3.place(relx=0.1, rely=0.8)

    def forest_back_zver():
        global photo
        image = Image.open('СилуэтНазад.png')  # вы подошли, но ничего не произошло
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        starter.place_forget()
        but1['text'] = 'Пойти направо'
        but1['command'] = home
        but1.place(relx=0.7, rely=0.8)
        but2.place_forget()
        but3['text'] = 'Пойти налево'
        but3['command'] = village
        but3.place(relx=0.1, rely=0.8)

    image = Image.open('Силуэт.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    but1['text'] = 'Повернуть назад'
    but1['command'] = forest_back
    but1.place(relx=0.7, rely=0.8)
    but2['text'] = 'Кинуть шишку'
    but2['command'] = death1
    but2.place(relx=0.4, rely=0.8)
    but3['text'] = 'Подойти поближе'
    but3['command'] = forest_back_zver
    but3.place(relx=0.1, rely=0.8)


def forest():
    global photo
    image = Image.open('Лес.png')
    image = image.resize(PICSIZE)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    starter.place_forget()
    but1['text'] = 'Пойти направо'
    but1.place(relx=0.7, rely=0.8)
    but1['command'] = home
    but2['text'] = 'Пойти прямо'
    but2.place(relx=0.4, rely=0.8)
    but2['command'] = polana
    but3['text'] = 'Пойти налево'
    but3.place(relx=0.1, rely=0.8)
    but3['command'] = village
    if flag_good_magik == 1:
        image = Image.open('ДобрыйКолдунНазад.png')
        image = image.resize(PICSIZE)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)


starter = tk.Button(master=window, text='Начать игру', width=40, height=10, command=forest)
starter.place(relx=0.4, rely=0.4)

but1 = tk.Button(master=window, text=' ', width=30, height=5)
but2 = tk.Button(master=window, text=' ', width=30, height=5)
but3 = tk.Button(master=window, text=' ', width=30, height=5)
but4 = tk.Button(master=window, text='Тишина', width=30, height=5)
but5 = tk.Button(master=window, text='Лютня', width=30, height=5)
but6 = tk.Button(master=window, text='Хор', width=30, height=5)

window.mainloop()
