def worst_fit(mem_avail, req, index):
    if not mem_avail:
        return None  
    
    max_index = None
    max_size = -1
    
    for i, (base, limit) in enumerate(mem_avail):
        size = limit - base
        if size >= req and size > max_size:
            max_size = size
            max_index = i
    
    if max_index is None:
        return None  

    base, limit = mem_avail[max_index]
    new_base = base
    new_limit = base + req
    
    if new_limit == limit:
        mem_avail.pop(max_index)  
    else:
        mem_avail[max_index] = (new_limit, limit)  
    
    return mem_avail, new_base, new_limit, max_index

#Ejemplo de uso
"""
if __name__ == "__main__":
    mem_avail = [(0, 100), (150, 400), (500, 900)]
    req = 120
    index = 0  

    result = worst_fit(mem_avail, req, index)
    print("Resultado:", result)
"""