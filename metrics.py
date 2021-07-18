def metrics(u, v):
    """
    Given two vectors u and v, compute the following distances/norm between
    the two and return them.
    - l1 Distance (norm)
    - l2 Distance (norm)

    If the two vectors have different dimensions,
    you should raise a ValueError

    :param u: first vector (list)
    :param v: second vector (list)
    :return: l1 distance, l2 distance
    :rtype: float, float
    :raise ValueError:
    """
    if len(u) != len(v):
        raise ValueError("The dimensions must be equal")
    else:
        def l2(u, v):
            distance = (((v[0]- u[0])**2) + ((v[1] - u[1])**2 ))**0.5
            print(distance)
            dist = 0
            for u, v in zip(u, v):
                squared = (v-u)**2 
                dist+=squared

            dist =dist**0.5
            print(f'L2 ={dist}')
            dist = float(dist)
        
        def l1(u, v):
            tom = 0
            for u, v in zip(u, v):
                summy = abs(v-u)
                tom +=summy

            print(f'L1 ={tom}')
            tom = float(tom)
            return tom
        
        l1(u,v)
        l2(u,v)
    
    # dotproduct=0
    # for u,v in zip(u,v):
    #     dotproduct = dotproduct+u*v
    # print('Dot product is:', dotproduct)
metrics ([0,3,4],[-2,4,1])