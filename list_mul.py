def list_mul(u, v):
    """
    Given two vectors, calculate and return the following quantities:
    - element-wise sum
    - element-wise product
    - dot product

    If the two vectors have different dimensions,
    you should raise a ValueError

    :param u: first vector (list)
    :param v: second vector (list)
    :return: the three quantities above
    :rtype: list, list, float
    :raise ValueError:
    """
    if len(u) == len(v):
        def element_wise_sum(u, v):
            

                uv = []                        #Create empty list
                for i in range(0, len(u)):
                    #Adds each element to the list
                    uv.append(u[i]+v[i]) 
                print(uv)
                element_wise_sum = uv
                return element_wise_sum   
          


        def element_wise_product(u, v):
            if len(u) == len(v):
    
                uv = []                        #Create empty list
                for i in range(0, len(u)):
                    #Adds each element to the list
                    uv.append(u[i]*v[i]) 
                print(uv)
                element_wise_product = uv
                return element_wise_product   
            else:
                raise ValueError("Different lengths")
        

    
        def dot_product(u, v):
            dotproduct=0
            for u,v in zip(u,v):
                dotproduct = float(dotproduct+u*v)
            print(dotproduct)
            return dotproduct

        
        element_wise_product = element_wise_product(u,v) 
        element_wise_sum = element_wise_sum(u,v)
        dot_product =dot_product(u,v)
        # raise NotImplementedError
        return(element_wise_sum, element_wise_product, dot_product)
    else:
        raise ValueError("Different lengths")

list_mul([5,6,7],[6,74,5])