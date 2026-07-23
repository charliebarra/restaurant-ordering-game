import turtle
import random

'''SETUP'''
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=1280,height=720)

money_writer = turtle.Turtle()
money_writer.hideturtle()
money_writer.penup()

stat_writer = turtle.Turtle()
stat_writer.hideturtle()
stat_writer.penup()

money = 10000000
topping_dict = {"Tomato Sauce": {"base_income": 1, "total_income": 1, "upgrade": 15, "owned": 1},
                "Cheese": {"base_income": 10, "total_income": 0, "upgrade": 100, "owned": 0},
                "Pepperoni": {"base_income": 80, "total_income": 0, "upgrade": 1100, "owned": 0},
                "Sausage": {"base_income": 470, "total_income": 0, "upgrade": 12000, "owned": 0},
                "Chicken": {"base_income": 2600, "total_income": 0, "upgrade": 130000, "owned": 0},
                "Pineapple": {"base_income": 14000, "total_income": 0, "upgrade": 1400000, "owned": 0}

        }

'''GAMLOOP'''
def main():
    def draw_main_menu():#REQ: Title, Start, Exit, Tutorial
        '''Backdrop'''
        t = turtle.Turtle()
        t.pensize(1)
        t.speed(-1)
        t.penup()
        t.goto(-640,-360)
        t.pendown()
        t.begin_fill()
        t.fillcolor('LightGoldenRodYellow')
        t.goto(640,-360)
        t.goto(640,360)
        t.goto(-640,360)
        t.goto(-640,-360)
        t.end_fill()

        '''Button Clicked Actions'''
        def start_button_click(x,y):
            draw_game_main()
            start_button.hideturtle()
            exit_button.hideturtle()
            text_writer.clear()
        
        def exit_button_click(x,y):
            exit()
        
        '''Button Setup'''
        start_button = turtle.Turtle()
        start_button.pensize(0)
        start_button.speed(-1)
        start_button.shape('circle')
        start_button.shapesize(stretch_wid=4, stretch_len=6)
        start_button.fillcolor('LightBlue')
        start_button.penup()
        start_button.goto(0,50)
        start_button.onclick(start_button_click)
            

        exit_button = turtle.Turtle()
        exit_button.pensize(0)
        exit_button.speed(-1)
        exit_button.shape('circle')
        exit_button.shapesize(stretch_wid=4, stretch_len=6)
        exit_button.fillcolor('IndianRed1')
        exit_button.penup()
        exit_button.goto(0,-50)
        exit_button.onclick(exit_button_click)

        '''Text'''
        text_writer = turtle.Turtle()
        text_writer.hideturtle()
        text_writer.penup()

        text_writer.goto(0, 150)
        text_writer.write("Charlie's Pizzeria", align="center", font=("Courier New", 36, "bold"))

        text_writer.goto(0, 42)
        text_writer.write("BEGIN", align="center", font=("Courier New", 15, "bold"))

        text_writer.goto(0, -58)
        text_writer.write("EXIT", align="center", font=("Courier New", 15, "bold"))

    def draw_customer_window():#REQ: #Shows the current order
        global customer_order, topping_dict
        '''Backdrop'''
        t = turtle.Turtle()
        t.pensize(1)
        t.speed(-1)
        t.penup()
        t.goto(-640,-360)
        t.pendown()
        t.begin_fill()
        t.fillcolor('lavenderblush')
        t.goto(-400,-360)
        t.goto(-400,360)
        t.goto(-640,360)
        t.goto(-640,-360)
        t.end_fill()

        '''Text'''
        text_writer = turtle.Turtle()
        text_writer.hideturtle()
        text_writer.penup()

        text_writer.goto(-520,300)
        text_writer.write("RECIPT", align="center", font=("Courier New", 30, 'bold'))


        '''Order List'''
        topping_selection = [] #Unlocked toppings
        text_writer.goto(-520,280)

        for i in topping_dict:
            if topping_dict[i]['owned'] > 0:
                topping_selection.append(i)
        
        amt_toppings = random.randint(1,len(topping_selection)) #Amount of toppings allowed to be on pizza
        customer_order = [] #Order Randomly chosen by customer

        for i in range(amt_toppings): #Loop that picks customer order
            add_customer_order = random.choice(topping_selection) #Picks a random topping
            customer_order.append(add_customer_order) #Adds random topping to order
            topping_selection.remove(add_customer_order) #Removes chosing topping from selection to prevent repeats

            #Writes Text
            text_writer.setheading(270) 
            text_writer.forward(25)
            text_writer.write("~"+customer_order[i], align="center", font=("Courier New", 15, 'normal'))

    def draw_market_window():#REQ Shows differnet purchaseable toppings
        '''Button Clicked Actions'''
        def tomatosauce_upgrade_click(x,y):
            global money, topping_dict, money_writer

            if money >= topping_dict["Tomato Sauce"]["upgrade"] * 1.15 ** topping_dict["Tomato Sauce"]["owned"]:
                money -= (topping_dict["Tomato Sauce"]["upgrade"] * 1.15 ** topping_dict["Tomato Sauce"]["owned"])
                topping_dict['Tomato Sauce']['owned'] += 1
                topping_dict['Tomato Sauce']['total_income'] = (topping_dict['Tomato Sauce']['base_income'] * topping_dict['Tomato Sauce']['owned'])

                money_writer.clear()
                money_writer.goto(0,300)
                money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))
                draw_upgrade_costs()

        def cheese_upgrade_click(x,y):
            global money, topping_dict, money_writer

            if money >= topping_dict["Cheese"]["upgrade"] * 1.15 ** topping_dict["Cheese"]["owned"]:
                money -= (topping_dict["Cheese"]["upgrade"] * 1.15 ** topping_dict["Cheese"]["owned"])
                topping_dict['Cheese']['owned'] += 1
                topping_dict['Cheese']['total_income'] = (topping_dict['Cheese']['base_income'] * topping_dict['Cheese']['owned'])

                money_writer.clear()
                money_writer.goto(0,300)
                money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))
                draw_upgrade_costs()

        def pepperoni_upgrade_click(x,y):
            global money, topping_dict, money_writer

            if money >= topping_dict["Pepperoni"]["upgrade"] * 1.15 ** topping_dict["Pepperoni"]["owned"]:
                money -= (topping_dict["Pepperoni"]["upgrade"] * 1.15 ** topping_dict["Pepperoni"]["owned"])
                topping_dict['Pepperoni']['owned'] += 1
                topping_dict['Pepperoni']['total_income'] = (topping_dict['Pepperoni']['base_income'] * topping_dict['Pepperoni']['owned'])

                money_writer.clear()
                money_writer.goto(0,300)
                money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))
                draw_upgrade_costs()

        def sausage_upgrade_click(x,y):
            global money, topping_dict, money_writer

            if money >= topping_dict["Sausage"]["upgrade"] * 1.15 ** topping_dict["Sausage"]["owned"]:
                money -= (topping_dict["Sausage"]["upgrade"] * 1.15 ** topping_dict["Sausage"]["owned"])
                topping_dict['Sausage']['owned'] += 1
                topping_dict['Sausage']['total_income'] = (topping_dict['Sausage']['base_income'] * topping_dict['Sausage']['owned'])

                money_writer.clear()
                money_writer.goto(0,300)
                money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))
                draw_upgrade_costs()
        
        def chicken_upgrade_click(x,y):
            global money, topping_dict, money_writer

            if money >= topping_dict["Chicken"]["upgrade"] * 1.15 ** topping_dict["Chicken"]["owned"]:
                money -= (topping_dict["Chicken"]["upgrade"] * 1.15 ** topping_dict["Chicken"]["owned"])
                topping_dict['Chicken']['owned'] += 1
                topping_dict['Chicken']['total_income'] = (topping_dict['Chicken']['base_income'] * topping_dict['Chicken']['owned'])

                money_writer.clear()
                money_writer.goto(0,300)
                money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))
                draw_upgrade_costs()

        '''Backdrop'''
        t = turtle.Turtle()
        t.pensize(1)
        t.speed(-1)
        t.penup()
        t.goto(640,-360)
        t.pendown()
        t.begin_fill()
        t.fillcolor('lavenderblush')
        t.goto(400,-360)
        t.goto(400,360)
        t.goto(640,360)
        t.goto(640,-360)
        t.end_fill()

        '''Button Setup'''
        tomatosauce_upgrade = turtle.Turtle()
        tomatosauce_upgrade.pensize(0)
        tomatosauce_upgrade.speed(-1)
        tomatosauce_upgrade.shape('square')
        tomatosauce_upgrade.shapesize(stretch_wid=3, stretch_len=8)
        tomatosauce_upgrade.fillcolor('FireBrick1')
        tomatosauce_upgrade.penup()
        tomatosauce_upgrade.goto(520,300)
        tomatosauce_upgrade.onclick(tomatosauce_upgrade_click)

        cheese_upgrade = turtle.Turtle()
        cheese_upgrade.pensize(0)
        cheese_upgrade.speed(-1)
        cheese_upgrade.shape('square')
        cheese_upgrade.shapesize(stretch_wid=3, stretch_len=8)
        cheese_upgrade.fillcolor('yellow')
        cheese_upgrade.penup()
        cheese_upgrade.goto(520,200)
        cheese_upgrade.onclick(cheese_upgrade_click)

        pepperoni_upgrade = turtle.Turtle()
        pepperoni_upgrade.pensize(0)
        pepperoni_upgrade.speed(-1)
        pepperoni_upgrade.shape('square')
        pepperoni_upgrade.shapesize(stretch_wid=3, stretch_len=8)
        pepperoni_upgrade.fillcolor('red')
        pepperoni_upgrade.penup()
        pepperoni_upgrade.goto(520,100)
        pepperoni_upgrade.onclick(pepperoni_upgrade_click)

        sausage_upgrade = turtle.Turtle()
        sausage_upgrade.pensize(0)
        sausage_upgrade.speed(-1)
        sausage_upgrade.shape('square')
        sausage_upgrade.shapesize(stretch_wid=3, stretch_len=8)
        sausage_upgrade.fillcolor('salmon4')
        sausage_upgrade.penup()
        sausage_upgrade.goto(520,0)
        sausage_upgrade.onclick(sausage_upgrade_click)

        chicken_upgrade = turtle.Turtle()
        chicken_upgrade.pensize(0)
        chicken_upgrade.speed(-1)
        chicken_upgrade.shape('square')
        chicken_upgrade.shapesize(stretch_wid=3, stretch_len=8)
        chicken_upgrade.fillcolor('peru')
        chicken_upgrade.penup()
        chicken_upgrade.goto(520,-100)
        chicken_upgrade.onclick(chicken_upgrade_click)

        '''Text'''
        text_writer = turtle.Turtle()
        text_writer.hideturtle()
        text_writer.penup()

        draw_upgrade_costs()

    def draw_topping_station():#REQ: Roll Pizza, Buttons for toppings, Send out Order
        global tomatosauce_button, cheese_button, pepperoni_button, sausage_button, chicken_button

        '''Button Clicked Actions'''
        def tomatosauce_button_click(x,y):
            tomatosauce_button.goto(0,-180)
            tomatosauce_button.begin_fill()
            tomatosauce_button.fillcolor('FireBrick1')
            tomatosauce_button.circle(180)
            tomatosauce_button.end_fill()
            tomatosauce_button.goto(-300,300)
            tomatosauce_button.fillcolor('gray10')

        def cheese_button_click(x,y):
            cheese_button.goto(0,-170)
            cheese_button.begin_fill()
            cheese_button.fillcolor('yellow')
            cheese_button.circle(170)
            cheese_button.end_fill()
            cheese_button.goto(-300,200)
            cheese_button.fillcolor('gray10')

        def pepperoni_button_click(x,y):
            pepperoni_button.goto(90,30)
            pepperoni_button.begin_fill()
            pepperoni_button.fillcolor('red')
            pepperoni_button.circle(50)
            pepperoni_button.end_fill()

            pepperoni_button.goto(-80,40)
            pepperoni_button.begin_fill()
            pepperoni_button.fillcolor('red')
            pepperoni_button.circle(50)
            pepperoni_button.end_fill()

            pepperoni_button.goto(-40,-100)
            pepperoni_button.begin_fill()
            pepperoni_button.fillcolor('red')
            pepperoni_button.circle(50)
            pepperoni_button.end_fill()

            pepperoni_button.goto(-300,100)
            pepperoni_button.fillcolor('gray10')
        
        def sausage_button_click(x,y):
            sausage_button.goto(80,20)
            sausage_button.begin_fill()
            sausage_button.fillcolor('salmon4')
            sausage_button.circle(48)
            sausage_button.end_fill()

            sausage_button.goto(-80,10)
            sausage_button.begin_fill()
            sausage_button.fillcolor('salmon4')
            sausage_button.circle(46)
            sausage_button.end_fill()

            sausage_button.goto(50,-130)
            sausage_button.begin_fill()
            sausage_button.fillcolor('salmon4')
            sausage_button.circle(45)
            sausage_button.end_fill()

            sausage_button.goto(-300,0)
            sausage_button.fillcolor('gray10')

        def chicken_button_click(x,y):
            chicken_button.goto(80,20)
            chicken_button.begin_fill()
            chicken_button.fillcolor('peru')
            chicken_button.circle(48)
            chicken_button.end_fill()

            chicken_button.goto(-80,10)
            chicken_button.begin_fill()
            chicken_button.fillcolor('peru')
            chicken_button.circle(46)
            chicken_button.end_fill()

            chicken_button.goto(50,-130)
            chicken_button.begin_fill()
            chicken_button.fillcolor('peru')
            chicken_button.circle(45)
            chicken_button.end_fill()

            chicken_button.goto(-300,-100)
            chicken_button.fillcolor('peru')

        '''Backdrop'''
        t = turtle.Turtle()
        t.pensize(1)
        t.speed(-1)
        t.penup()
        t.goto(-400,-360)
        t.pendown()
        t.begin_fill()
        t.fillcolor('LightGoldenRodYellow')
        t.goto(400,-360)
        t.goto(400,360)
        t.goto(-400,360)
        t.goto(-400,-360)
        t.end_fill()

        '''Button Setup'''
        tomatosauce_button = turtle.Turtle()
        tomatosauce_button.pensize(0)
        tomatosauce_button.speed(-1)
        tomatosauce_button.shape('circle')
        tomatosauce_button.shapesize(stretch_wid=3, stretch_len=5)
        tomatosauce_button.fillcolor('FireBrick1')
        tomatosauce_button.penup()
        tomatosauce_button.goto(-300,300)
        tomatosauce_button.onclick(tomatosauce_button_click)

        cheese_button = turtle.Turtle()
        cheese_button.pensize(0)
        cheese_button.speed(-1)
        cheese_button.shape('circle')
        cheese_button.shapesize(stretch_wid=3, stretch_len=5)
        cheese_button.fillcolor('yellow')
        cheese_button.penup()
        cheese_button.goto(-300,200)
        cheese_button.onclick(cheese_button_click)
        
        pepperoni_button = turtle.Turtle()
        pepperoni_button.pensize(0)
        pepperoni_button.speed(-1)
        pepperoni_button.shape('circle')
        pepperoni_button.shapesize(stretch_wid=3, stretch_len=5)
        pepperoni_button.fillcolor('red')
        pepperoni_button.penup()
        pepperoni_button.goto(-300,100)
        pepperoni_button.onclick(pepperoni_button_click)

        sausage_button = turtle.Turtle()
        sausage_button.pensize(0)
        sausage_button.speed(-1)
        sausage_button.shape('circle')
        sausage_button.shapesize(stretch_wid=3, stretch_len=5)
        sausage_button.fillcolor('salmon4')
        sausage_button.penup()
        sausage_button.goto(-300,0)
        sausage_button.onclick(sausage_button_click)

        chicken_button = turtle.Turtle()
        chicken_button.pensize(0)
        chicken_button.speed(-1)
        chicken_button.shape('circle')
        chicken_button.shapesize(stretch_wid=3, stretch_len=5)
        chicken_button.fillcolor('peru')
        chicken_button.penup()
        chicken_button.goto(-300,-100)
        chicken_button.onclick(chicken_button_click)

        '''Text'''
        text_writer = turtle.Turtle()
        text_writer.hideturtle()
        text_writer.penup()

        text_writer.goto(-300, 330)
        text_writer.write("Tomato Sauce", align="center", font=("Courier New", 11, 'normal'))

        text_writer.goto(-300, 230)
        text_writer.write("Cheese", align="center", font=("Courier New", 11, 'normal'))

        text_writer.goto(-300, 130)
        text_writer.write("Pepperoni", align="center", font=("Courier New", 11, 'normal'))

        text_writer.goto(-300, 30)
        text_writer.write("Sausage", align="center", font=("Courier New", 11, 'normal'))

        text_writer.goto(-300, -70)
        text_writer.write("Chicken", align="center", font=("Courier New", 11, 'normal'))

    def draw_upgrade_costs():
        global topping_dict, stat_writer

        '''Text'''
        stat_writer.clear()

        #Tomato Sauce
        stat_writer.goto(430, 290)
        stat_writer.write(topping_dict['Tomato Sauce']['owned'], align="center", font=("Courier New", 14, 'bold'))
        stat_writer.goto(520, 330)
        stat_writer.write('Tomato Sauce', align="center", font=("Courier New", 11, 'normal'))
        stat_writer.goto(520,250)
        stat_writer.write(f'${topping_dict["Tomato Sauce"]["upgrade"] * 1.15 ** topping_dict["Tomato Sauce"]["owned"]:,.2f}', align="center", font=("Courier New", 11, 'normal'))

        #Cheese
        stat_writer.goto(430, 190)
        stat_writer.write(topping_dict['Cheese']['owned'], align="center", font=("Courier New", 14, 'bold'))
        stat_writer.goto(520, 230)
        stat_writer.write('Cheese', align="center", font=("Courier New", 11, 'normal'))
        stat_writer.goto(520,150)
        stat_writer.write(f'${topping_dict["Cheese"]["upgrade"] * 1.15 ** topping_dict["Cheese"]["owned"]:,.2f}', align="center", font=("Courier New", 11, 'normal'))

        #Pepperoni
        stat_writer.goto(430, 90)
        stat_writer.write(topping_dict['Pepperoni']['owned'], align="center", font=("Courier New", 14, 'bold'))
        stat_writer.goto(520, 130)
        stat_writer.write('Pepperoni', align="center", font=("Courier New", 11, 'normal'))
        stat_writer.goto(520,50)
        stat_writer.write(f'${topping_dict["Pepperoni"]["upgrade"] * 1.15 ** topping_dict["Pepperoni"]["owned"]:,.2f}', align="center", font=("Courier New", 11, 'normal'))

        #Sausage
        stat_writer.goto(430, -10)
        stat_writer.write(topping_dict['Sausage']['owned'], align="center", font=("Courier New", 14, 'bold'))
        stat_writer.goto(520, 30)
        stat_writer.write('Sausage', align="center", font=("Courier New", 11, 'normal'))
        stat_writer.goto(520,-50)
        stat_writer.write(f'${topping_dict["Sausage"]["upgrade"] * 1.15 ** topping_dict["Sausage"]["owned"]:,.2f}', align="center", font=("Courier New", 11, 'normal'))

        #Chicken
        stat_writer.goto(430, -110)
        stat_writer.write(topping_dict['Chicken']['owned'], align="center", font=("Courier New", 14, 'bold'))
        stat_writer.goto(520, -70)
        stat_writer.write('Chicken', align="center", font=("Courier New", 11, 'normal'))
        stat_writer.goto(520,-150)
        stat_writer.write(f'${topping_dict["Chicken"]["upgrade"] * 1.15 ** topping_dict["Chicken"]["owned"]:,.2f}', align="center", font=("Courier New", 11, 'normal'))

    def draw_game_main():#REQ: Reset topiing station, Print money
        global money_writer
        '''Button Clicked Actions'''
        def finalize_button_clicked(x,y):
            global money, topping_dict
            
            if tomatosauce_button.fillcolor() == ('gray10') and 'Tomato Sauce' in customer_order:
                money += topping_dict['Tomato Sauce']["total_income"]
            tomatosauce_button.fillcolor('FireBrick1')

            if cheese_button.fillcolor() == ('gray10') and 'Cheese' in customer_order:
                money += topping_dict['Cheese']["total_income"]
            cheese_button.fillcolor('yellow')

            if pepperoni_button.fillcolor() == ('gray10') and 'Pepperoni' in customer_order:
                money += topping_dict['Pepperoni']["total_income"]
            pepperoni_button.fillcolor('red')

            if sausage_button.fillcolor() == ('gray10') and 'Sausage' in customer_order:
                money += topping_dict['Sausage']["total_income"]
            sausage_button.fillcolor('salmon4')

            if chicken_button.fillcolor() == ('gray10') and 'Chicken' in customer_order:
                money += topping_dict['Chicken']["total_income"]
            chicken_button.fillcolor('peru')
            
            #Redraw Pizza Dough
            t.goto(0,-200)
            t.begin_fill()
            t.fillcolor('burlywood2')
            t.circle(200)
            t.end_fill()
            
            #Redraw Money
            money_writer.clear()
            money_writer.goto(0,300)
            money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))

            draw_customer_window()
            

        '''Backdrop'''
        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(1)
        t.speed(-1)
        t.penup()
        t.goto(-640,-360)
        t.pendown()
        t.begin_fill()
        t.fillcolor('black')
        t.goto(640,-360)
        t.goto(640,360)
        t.goto(-640,360)
        t.goto(-640,-360)
        t.end_fill()
        t.penup()

        '''Game Windows'''
        draw_customer_window()
        draw_topping_station()
        draw_market_window()

        t.pendown
        t.goto(0,-200)
        t.begin_fill()
        t.fillcolor('burlywood2')
        t.circle(200)
        t.end_fill()

        '''Button Setup'''
        finalize_button = turtle.Turtle()
        finalize_button.pensize(0)
        finalize_button.speed(-1)
        finalize_button.shape('circle')
        finalize_button.shapesize(stretch_wid=4, stretch_len=5)
        finalize_button.fillcolor('LightGreen')
        finalize_button.penup()
        finalize_button.goto(300,-250)
        finalize_button.onclick(finalize_button_clicked)

        '''Text'''
        text_writer = turtle.Turtle()
        text_writer.hideturtle()
        text_writer.penup()

        money_writer.goto(0,300)
        money_writer.write((f"${money:,.2f}"), align="center", font=("Courier New", 30, 'bold'))

        text_writer.goto(300, -310)
        text_writer.write("Finalize", align="center", font=("Courier New", 11, 'normal'))

    draw_main_menu()
main()

'''END'''
turtle.done()
