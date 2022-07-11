from currencies import Currency


def discount(user_input, discount_percentage):

    price = float(user_input[0])
    currency_sign = Currency(user_input[1])

    discount_sum = discount_percentage / 100 * price
    final_price = price - discount_sum

    return f"Discount: {discount_percentage:.2f}% -> {currency_sign.get_money_format(f'{discount_sum:.2f}')}\nFinal " \
           f"price: {currency_sign.get_money_format(f'{final_price:.2f}')}"


user_input = input("Please enter the price and the respective currency separated by single space:\n").split()
price_discount = float(input("Please enter the discount by which you want to reduce the price:\n"))

print(discount(user_input, price_discount))
