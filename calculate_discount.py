
#Write code for customer input
original_price= input('enter price:')
discount_percentage= input('enter percentage:')

#Define your variables, converting your variables when needed
discount_decimal=float(discount_percentage)/100.0
discount_amount=float(original_price)*float(discount_decimal)
final_price=float(original_price)-float(discount_amount)

#Using the if and else function to carry out your coding
if float(discount_percentage) >= 20:
	print("Discount amount:", discount_amount)
	print(f"final price: {final_price}")
else:
	print("No discount applied or discount less than 20%.")
	print("original price:", original_price)
