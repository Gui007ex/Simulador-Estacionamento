from Data.Base_handle import Value
from Data.Data_handle import limits

def SearchState(plaque):
    value = Value(plaque[:3])
    for state in limits:
        for limit in limits[state]:
            min_val, max_val = Value(limit[0]), Value(limit[1])
            if min_val <= value <= max_val:
                return state
    return "Não encontrado"
