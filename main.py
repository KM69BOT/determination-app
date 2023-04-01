from tkinter import *
import random
from pathlib import Path
import sys

Motivations = [
    "You are capable of achieving great things.",
    "Your unique perspective is valuable to the world.",
    "You are worthy of love and respect.",
    "You have the power to create positive change.",
    "You are stronger than you realize.",
    "Your efforts make a difference, even if it doesn't seem like it.",
    "You have a purpose in life.",
    "You are more resilient than you think.",
    "You are capable of overcoming any obstacle.",
    "Your happiness is important and worth pursuing.",
    "You are a work in progress, and that's okay.",
    "You have a bright future ahead of you.",
    "Your dreams are worth pursuing.",
    "You are a valuable member of your community.",
    "You have the power to make a difference in someone else's life.",
    "You are capable of learning and growing.",
    "Your accomplishments deserve recognition and celebration.",
    "You have a unique set of skills and talents.",
    "You are capable of adapting to new situations.",
    "You are deserving of success and happiness.",
    "You have the ability to make your dreams a reality.",
    "Your voice deserves to be heard.",
    "You are not defined by your past mistakes.",
    "You have the power to forgive and let go of grudges.",
    "You are capable of making positive changes in your life.",
    "You have the strength to face difficult challenges.",
    "You are capable of achieving balance in your life.",
    "You have the power to inspire others.",
    "You are capable of being kind and compassionate to others.",
    "You have the ability to find joy in the little things.",
    "You are capable of creating meaningful relationships with others.",
    "You have the power to make a positive impact in the world.",
    "You have the ability to persevere through tough times.",
    "You are capable of being a great leader.",
    "You have the power to bring people together.",
    "You are capable of making a difference in your workplace.",
    "Your hard work and dedication will pay off.",
    "You have the ability to find solutions to difficult problems.",
    "You are capable of making difficult decisions.",
    "You have the power to create a better future for yourself and others.",
    "You have the ability to stay calm in stressful situations.",
    "You are capable of finding meaning and purpose in your life.",
    "You have the power to overcome fear and doubt.",
    "You have the ability to learn from your mistakes.",
    "You are capable of making positive changes in your behavior.",
    "You have the power to forgive yourself for past mistakes.",
    "You have the ability to build resilience and bounce back from setbacks.",
    "You are capable of achieving balance in your emotions.",
    "You have the power to make a difference in the lives of those around you.",
    "You have the ability to let go of negative self-talk.",
    "You are capable of building healthy habits and routines.",
    "You have the power to maintain positive relationships with others.",
    "You have the ability to communicate effectively with others.",
    "You are capable of setting and achieving goals.",
    "You have the power to find meaning in your work.",
    "You have the ability to embrace change and adapt to new situations.",
    "You are capable of finding joy in the present moment.",
    "You have the power to overcome self-doubt and negative thoughts.",
    "You have the ability to take control of your life and make positive changes.",
    "You are capable of finding purpose and meaning in difficult times.",
    "You have the power to make a difference in the lives of those who need it", ]


def GetResource(path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        return path
    else:
        return base_path.joinpath(path)


def ChangeMotivation():
    if RefreshButton.cget('text') == "Begin":
        RefreshButton.config(text="Refresh")
        RefreshButton.update()
        Text.config(text=Motivations[random.randint(0, 60)])

    else:
        Text.config(text=Motivations[random.randint(0, 60)])


root = Tk()
root.resizable(0, 0)
root.title("")
root.geometry("500x250")
IconPath = GetResource(r".\heart.ico")
root.iconbitmap(IconPath)

Text = Label(text="You matter", font=("Arial", 18), wraplength=450)
Text.place(relx=0.5,
           rely=0.40,
           anchor="center")

RefreshButton = Button(text="Begin", command=ChangeMotivation)
RefreshButton.place(relx=0.5,
                    rely=0.70,
                    anchor="center")

root.mainloop()
