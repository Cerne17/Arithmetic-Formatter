from typing import List
def arithmatic_arranger(list_of_operations: List[str], show_result: bool):
    '''
    Input Format: ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True
    '''
    # Solving the expression
    if show_result:
        for operation in list_of_operations:
            operator: str = operation.split(" ")[1]
            display_operation_with_result(operation, operator)
    else:
        for operation in list_of_operations:
            display_operation(operation)

arithmatic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

def display_operation(operation: str):
    return 0
    

def display_operation_with_result(operation: str, operator: str):
    return 0

def find_longest_operand(operation: str):
    first_operand: str = operation.split(" ")[0]
    second_operand: str = operation.split(" ")[2]

    first_operand_length: int = len(first_operand)
    second_operand_length: int = len(second_operand)

    if first_operand_length > second_operand_length:
        return (first_operand, first_operand_length)
    else:
        return (second_operand, second_operand_length)

def solve_operation(operation: str, operator: str) -> str:
    if operator in ['+', '-']:
        return str(eval(operation))
    else:
        raise Exception("Invalid Operator")
