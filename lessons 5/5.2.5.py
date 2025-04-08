price_sir = 60
price_icecream = 20
money = int(input("Скольо дала денег мама? "))

if money >= price_sir:
    money -= price_sir
    print("На сыр денег хватило")
    if money >= price_icecream:
        money -= price_icecream
        print("И на мороженное хватило!")
    else:
        print("Денег малова-то для покупки мороженного")
else:
    print("Даже не хватило на сыр")
