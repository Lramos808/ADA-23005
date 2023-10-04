def go_down(CURRENT_NODE):
    right([LAYER_DOWN][STEP_RIGHT])
    left([LAYER_DOWN][SAME_LOCATION])
    
def go_right(current:Node):
    if current.cost_of_route < COST_OF_STEP:
        if (GO_DOWN_BOUNDRY not HIT):
            current.cost_of_route += COST_OF_STEP
            go_down(NODE_DOWN_AND_RIGHT)
    return

def go_left(current:Node):
    if head.cost_of_route < COST_OF_STEP:
        if (GO_DOWN_BOUNDRY not HIT):
            current.cost_of_route += COST_OF_STEP
            go_down(NODE_DOWN_AND_LEFT)
    return
