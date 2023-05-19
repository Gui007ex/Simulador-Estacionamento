# Tol 15 min
# 10 até 3 horas
# 5 por hora a mais

from math import ceil

def CalcutatePrice(minutes):
    if minutes <= 15:
        return 0
    elif 15 < minutes <= 180:
        return 10
    else:
        return 10 + ceil(5*((minutes-180)/60))

def CalculateTicket(entry, exit):
    h_entry, m_entry = map(int, entry.split(':'))
    h_exit, m_exit = map(int, exit.split(':'))
    m_entry += h_entry * 60
    m_exit += h_exit * 60
    if m_exit < m_entry:
        m_exit += 24*60
    return CalcutatePrice(m_exit - m_entry)

print()