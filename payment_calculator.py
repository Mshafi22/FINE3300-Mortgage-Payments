# Mortgage payment calculator
def mortgage_payments(principal, rate, amortization):
    """
    This function calculates different mortgage payments based on:
    - Principal amount (loan amount)
    - Interest rate (as a percentage)
    - Amortization period (in years)

    It returns six different payment amounts:
    - Monthly
    - Semi-monthly
    - Bi-weekly
    - Weekly
    - Rapid Bi-weekly
    - Rapid Weekly
    """
     # Convert annual interest rate (as a percentage) to a decimal
    rq = rate / 100

    # Convert amortization period from years to months
    n_months = amortization * 12

    # Calculate periodic interest rates
    r_monthly = (1 + rq / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rq / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2 / 26) - 1
    r_weekly = (1 + rq / 2) ** (2 / 52) - 1
     # Function to calculate Present Value of Annuity (PVA)
    def pva(r, n):
     return (1 - (1 + r) ** -n) / r
     # Calculate mortgage payments
    monthly_payment = principal / pva(r_monthly, n_months)
    semi_monthly_payment = principal / pva(r_semi_monthly, n_months * 2)
    bi_weekly_payment = principal / pva(r_bi_weekly, n_months * 26 / 12)
    weekly_payment = principal / pva(r_weekly, n_months * 52 / 12)
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    return (
     round(monthly_payment, 2),
     round(semi_monthly_payment, 2),
     round(bi_weekly_payment, 2),
     round(weekly_payment, 2),
     round(rapid_bi_weekly_payment, 2),
     round(rapid_weekly_payment, 2)
 )
# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
amortization = int(input("Enter the amortization period (in years): "))

# Call the function and store the returned values
payments = mortgage_payments(principal, rate, amortization)

# Display results
print("\nMortgage Payment Schedule:")
print(f"Monthly Payment: ${payments[0]:.2f}")
print(f"Semi-monthly Payment: ${payments[1]:.2f}")
print(f"Bi-weekly Payment: ${payments[2]:.2f}")
print(f"Weekly Payment: ${payments[3]:.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:.2f}")