import queue as q
import stack as s


##################################################################################
#
# A queue that enqueues stacks!  #################################################
#
##################################################################################

print("\nA queue that enqueues stacks!\n")

# create new queue
queue = q.create()

# enqueue a bunch of stacks!
for i in range(0, 10):

    # make new stack
    new_stack = s.create()

    for j in range(0, 3):

        val = i * 3 + j

        print("Pushing value : " + str(val))
        s.push(new_stack, val)

    print("Enqueue-ing the stack containing those past 3 values onto the queue!!\n")
    q.enqueue(queue, new_stack)

print("\nDe-queue-ing the queue!\n")

# empty the queue
while not q.is_empty(queue):

    print("De-queue-ing a stack!")
    current_dequeued_stack = q.dequeue(queue)

    while not q.is_empty(current_dequeued_stack):
        print("Popped value from de-queued stack: " + str(s.pop(current_dequeued_stack)))

    print()   # Aesthetic

print("***********************************************")

##################################################################################
#
# A queue that enqueues queues!  #################################################
#
##################################################################################

print("\nA queue that enqueues queues!\n")

# create new queue
queue = q.create()

# enqueue a bunch of stacks!
for i in range(0, 10):

    # make new queue
    new_queue = q.create()

    for j in range(0, 3):

        val = i * 3 + j

        print("Enqueueing value : " + str(val))
        q.enqueue(new_queue, val)

    print("Enqueue-ing the queue containing those past 3 values onto the queue!!\n")
    q.enqueue(queue, new_queue)

print("\nDe-queue-ing the queue!\n")

# empty the queue
while not q.is_empty(queue):

    print("De-queue-ing a queue!")
    current_dequeued_queue = q.dequeue(queue)

    while not q.is_empty(current_dequeued_queue):
        print("De-queued value from de-queued queue: " + str(q.dequeue(current_dequeued_queue)))

    print()   # Aesthetic

print("***********************************************")

##################################################################################
#
# A stack that pushes queues!  ###################################################
#
##################################################################################

print("\nA stack that pushes queues!\n")

# create new stack
stack = s.create()

# Push a bunch of queues!
for i in range(0, 10):

    # make new queue
    new_queue = q.create()

    for j in range(0, 3):

        val = i * 3 + j

        print("Enqueueing value : " + str(val))
        q.enqueue(new_queue, val)

    print("Pushing the queue containing those past 3 values onto the stack!\n")
    s.push(stack, new_queue)

print("\nPopping the stack!\n")

# empty the stack
while not s.is_empty(stack):

    print("Popping a queue!")
    current_popped_queue = s.pop(stack)

    while not q.is_empty(current_popped_queue):
        print("De-queued value from popped queue: " + str(q.dequeue(current_popped_queue)))

    print()   # Aesthetic

print("***********************************************")

##################################################################################
#
# A stack that pushes stacks!  ###################################################
#
##################################################################################

print("\nA stack that pushes stacks!\n")

# create new stack
main_stack = s.create()

# Push a bunch of stacks!
for i in range(0, 10):

    # make new stack
    new_stack = s.create()

    for j in range(0, 3):

        val = i * 3 + j

        print("Pushing value : " + str(val))
        s.push(new_stack, val)

    print("Pushing the stack containing those past 3 values onto the main stack!\n")
    s.push(main_stack, new_stack)

print("\nPopping the main stack!\n")

# empty the main stack
while not s.is_empty(main_stack):

    print("Popping a stack!")
    current_popped_stack = s.pop(main_stack)

    while not s.is_empty(current_popped_stack):
        print("Popped value from popped stack: " + str(s.pop(current_popped_stack)))

    print()   # Aesthetic

