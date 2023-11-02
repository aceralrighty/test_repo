import datetime

date = datetime.date.today()

inputFile = open("./file/stadium_seating_income.txt", 'r')
outputFile = open("./file/discount_rates.txt", 'w+')

line = ""
tot_cost = ""
seat_qty = ""
seat_class = ""
class_code = ""

discountPerc = 0
finalPrice = 0

GrandTotal = 0
GrandQty = 0
FinalTotal = 0

page_ctr = 0
line_ctr = 0


def main():
    init()
    while line:
        calcs()
        output()
        input_data()
    grandtotal()


def heading():
    outputFile.write(f"Date: {date}               Stadium Seating           Page:   \n"
                     f"                          Discount Rates  Class\n"
                     ""
                     f"Class        Ticket Cost       Qty         Total         Discount Rate (%)        Final Price\n")


def init():
        global line, seat_class, seat_qty, class_code, tot_cost, line_ctr, page_ctr
        line = inputFile.readline()
        line_data = line.split("/")
        seat_class = line_data[0]
        class_code = line_data[1]
        seat_qty = line_data[2]
        tot_cost = line_data[3].rstrip('\n')

        line_ctr = 0
        page_ctr = 1
        heading()


def discount_a():
    global seat_qty, discountPerc, finalPrice, tot_cost
    if 25 <= int(seat_qty) < 100:
        discountPerc = '12%'
        finalPrice = float(tot_cost) * .12
    elif 100 <= int(seat_qty) < 175:
        discountPerc = '14%'
        finalPrice = float(tot_cost) * .14
    elif int(seat_qty) > 175:
        discountPerc = '15%'
        finalPrice = float(tot_cost) * .15


def discount_b():
    global seat_qty, discountPerc, finalPrice, tot_cost
    if 75 <= int(seat_qty) < 200:
        discountPerc = '12%'
        finalPrice = float(tot_cost) * .12
    elif 200 <= int(seat_qty) < 375:
        discountPerc = '14%'
        finalPrice = float(tot_cost) * .14
    elif int(seat_qty) > 375:
        discountPerc = '15%'
        finalPrice = float(tot_cost) * .15


def discount_c():
    global seat_qty, discountPerc, finalPrice, tot_cost
    if 200 <= int(seat_qty) < 400:
        discountPerc = '12%'
        finalPrice = float(tot_cost) * .12
    elif 400 <= int(seat_qty) < 650:
        discountPerc = '14%'
        finalPrice = float(tot_cost) * .14
    elif int(seat_qty) > 650:
        discountPerc = '15%'
        finalPrice = float(tot_cost) * .15


def calcs():
    global seat_class, seat_qty, finalPrice, tot_cost, GrandTotal, GrandQty, FinalTotal
    match seat_class:
        case 'ClassA':
            discount_a()
        case 'ClassB':
            discount_b()
        case 'ClassC':
            discount_c()

    finalPrice = float(tot_cost) - finalPrice

    GrandTotal += float(tot_cost)
    GrandQty += float(seat_qty)
    FinalTotal += finalPrice


def output():
    global seat_class, class_code, seat_qty, tot_cost, discountPerc, finalPrice, line_ctr
    outputFile.write(f"{seat_class}          ${float(class_code):.2f}           {seat_qty}       ${float(tot_cost):.2f}                 {discountPerc}              ${finalPrice:.2f}\n")

    line_ctr += 1


def input_data():
    global line, seat_class, seat_qty, class_code, tot_cost, tot_cost
    line = inputFile.readline()
    if line:
        line_data = line.split("/")
        seat_class = line_data[0]
        class_code = line_data[1]
        seat_qty = line_data[2]
        tot_cost = line_data[3]


def grandtotal():
    global GrandTotal, GrandQty, FinalTotal
    outputFile.write(f"Grand Total:       {GrandQty}         ${GrandTotal:.2f}        ${FinalTotal:.2f}")

main()