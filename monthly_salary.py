

#42%is basic pay

def get_basic_pay(amount):
    # res = 0.42*amount
    res = 0.51*amount
    print("base salary pm without cutting taxes:  ", res)
    return res


def get_remove_pf(amount):
    return amount - (0.24*amount)

def get_tax_amount(amount):
    tax = 0
    if amount > 2000000:
        rem = amount-2000000
        tax = 0.30*rem
    
    total_tax = 291000+tax
    return total_tax


def new_tax_amount(amount):
    tax = 0
    if amount > 2400000:
        rem = amount-2400000
        print(rem)
        tax += 0.30*rem
        print(tax)
    
    if amount > 2000000:
        rem = min(amount, 2400000) - 2000000
        print(rem)
        tax += 0.25*rem
        print(tax)
    

    print(f"new total tax is:   {tax+200000}")
    
    return tax + 200000
        


    


def get_montly_salary(amount):
    #amount: fixed ctc
    per_month = amount//12
    bpm = get_basic_pay(per_month)
    remaining = per_month - bpm
    after_pf = get_remove_pf(bpm)

    total_pm = remaining+after_pf

    per_year = 12*total_pm - 3000

    tax_amount = get_tax_amount(per_year)

    new_tax_amt = new_tax_amount(per_year)


    final_py = per_year - tax_amount-75000
    new_final_py = per_year - new_tax_amt-75000

    final_pm = final_py//12

    new_final_pm = new_final_py//12

    return final_pm, new_final_pm



ctc = [2000000,2300000, 2350000, 2400000, 2500000, 2600000, 2700000, 2800000, 3000000,3500000, 3600000, 4000000, 4100000, 4500000, 4800000, 5000000, 6000000, 7000000, 10000000]


for ct in ctc:
    per_month, new_final_pm = get_montly_salary(ct)
    print(f"for annual ctc of {ct}, the per month in hand is:  {per_month} new final per month in hand is:   {new_final_pm}")





