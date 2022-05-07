import streamlit as st

# Make page wide screen and set app title
st.set_page_config(layout="wide", page_title="Simple Savings Calculator")

# Header + intro info
st.title("Simple Savings Calculator")
st.info("Pardon my dust, this is still a work in progress!  Please stand by as I continue working on this but feel free to continue using this app!")
st.write("Welcome, this is a simple calculator that lets you calculate how much of your income you should transfer from your checking to your savings account.")
st.write("You can also put in any donations!")
st.warning("Please note: all of the inputs and results are in USD.  Hoping to implement other currencies in the future! :)")
st.write("")
st.write("")

# 2 columns; left side is calculator, right side is result
calc_cols = st.columns((3, 3))

# Global variables
calc_cols[0].header("Inputs")
total = calc_cols[0].number_input(label="Enter total checking amount", key="total_input")
income = calc_cols[0].number_input(label="Enter income", key="income_input")
donations = calc_cols[0].number_input(label="Put any other donations", key="donations_input")
st.write("")
# total = float(input('Enter total checking amount: $')) # $1301.10
# income = float(input('Enter income: $'))   # $1073.84
# missions = float(input('Put any missions giving: $'))    # $5.00
# print('\n')

# Global function, round results to nearest hundredth
def roundHouseLOL(x):
    ans = round(x, 2)                       # round arg to nearest hundredth (2 decimal places)
    return float('{0:.2f}'.format(ans))     # truncate output to 2 decimal places as float

# Savings + tithe + missions to make checking 600
calc_cols[1].header("Calculation results")
savings_tithe_donations = roundHouseLOL(total - 600)
calc_cols[1].write("amt to make checking $600 USD = " + str(savings_tithe_donations))
# print('amt to make checking $600 =', savings_tithe_donations)

# Tithing
tithe = roundHouseLOL(income * 0.10)
calc_cols[1].write("tithe fr income = $" + str(tithe))
# print('tithe fr income =', tithe)

# Transfer to savings w/o tithe + donations
savings = roundHouseLOL(savings_tithe_donations - tithe - donations)
calc_cols[1].write("any donations = $" + str(donations))
calc_cols[1].write("total giving = $" + str(tithe + donations))
calc_cols[1].write("transfer to savings = $" + str(savings))
# print('missions giving =', donations)
# print('total giving =', tithe + donations)
# print('transfer to savings =', savings)

# Result should equal $600 for amount left in checking
checkIt = roundHouseLOL(total - tithe - savings - donations)
checkItSteps = str(total) + " - " + str(tithe) + " - " + str(savings) + " - " + str(donations)
calc_cols[1].write("sanity check = $" + str(checkIt) + " = " + checkItSteps)
# print('sanity check =', checkIt)
# print('\n')