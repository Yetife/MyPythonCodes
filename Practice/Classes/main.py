import native

if __name__=="__main__":
    # native.register_native_to_cohort("John", "Doe", "John@gmail.com", "9083456711", "F")
    # native.register_native_to_cohort("John", "Doe", "John@gmail.com", "9083456711", "M")
    # native.register_native_to_cohort("John", "Doe", "John@gmail.com", "9083456711", "F")
    
    # print(native.cohort_eight)
    
    next_of_kin = []
    next_of_kin1 = native.create_next_of_kin("Tayo", "Oye", "273829010", "M", "Brother")
    next_of_kin.append(next_of_kin1)
    native.register_native_to_cohort("John", "Doe", "John@gmail.com", "9083456711", "F", next_of_kin)
    print(native.cohort_eight[0].next_of_kin[0].first_name)