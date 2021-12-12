import random as rd

def randomize_cohort(cohort_list, cohort_size, block_sizes):
    """
    Randomizes the order of the cohort list.
    """

    this_block = None
    print("apples")
    # TODO: ensure that cohort list nd block sizes are devisible
    if not this_block:
        this_block_size = block_sizes[rd.randint(0, len(block_sizes) - 1)]
        this_block = []
        block_multiplier = this_block_size / len(cohort_list)
        
        # For each cohort append an equal amount of values to this block
        for cohort in cohort_list:
            for i in range(int(block_multiplier)):
                this_block.append(cohort)
        
        print("Presuffle {}".format(this_block))
        rd.shuffle(this_block)
        print("Postshuffle {}".format(this_block))

    # for i in this_block:
    #     this_blco

# randomize_cohort(["a", "b"], 300, [4,6])


if __name__ == "__main__":
    # print("apples")
    randomize_cohort(["a", "b"], 300, [4,6])