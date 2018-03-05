def split_the_bill(gr):
    to_pay_each = sum(gr.values()) / len(gr.keys())

    for key, value in gr.items():
        gr[key] = to_pay_each - value

    return gr


group = {
    'Amy': 20,
    'Bill': 15,
    'Chris': 10
}
print(split_the_bill(group))  # { 'Amy': -5, 'Bill': 0, 'Chris': 5 }
