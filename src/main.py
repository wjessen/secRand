import random as rd

def randomize_cohort(cohort_list, cohort_size, block_sizes):
    """
    Randomizes the order of the cohort list.
    """
    full_list = []
    this_block = []

    if this_block.len() == 0:
        this_block = create_block(block_sizes, cohort_list)

    while this_block.len() > 0:
        full_list.append(this_block.pop(0))
    
    # for i in this_block:
    #     this_blco

# randomize_cohort(["a", "b"], 300, [4,6])

def create_block(block_sizes, cohort_list):
    """
    Creates a block of randomized cohorts.
    """
    this_block_size = block_sizes[rd.randint(0, len(block_sizes) - 1)]
    this_block = []
    block_multiplier = this_block_size / len(cohort_list)
    
    # For each cohort append an equal amount of values to this block
    for cohort in cohort_list:
        for i in range(int(block_multiplier)):
            this_block.append(cohort)
    
    return rd.shuffle(this_block)
    

if __name__ == "__main__":
    # print("apples")
    randomize_cohort(["a", "b"], 300, [4,6])