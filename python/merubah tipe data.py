#operator casting

#integer
data_int = 9
print(data_int)

data_float = float(data_int)
print(data_float)#akan menghasilkan 9.0 karena float dari integer

data_str = str(data_int)
print(data_str)#akan menghasilkan '9' karena string dari integer

data_bool = bool(data_int)
print(data_bool) #akan menghasilkan True karena integer selain 0 adalah True

#float
data_float = 9.9
print(data_float)

data_int = int(data_float)
print(data_int)#akan menghasilkan 9 karena integer dari float

data_str = str(data_float)
print(data_str)#akan menghasilkan '9.9' karena string dari float

data_bool = bool(data_float)
print(data_bool) #akan menghasilkan True karena float selain 0 adalah True

#string
data_str = "10"
print(data_str)

data_int = int(data_str)
print(data_int)#akan menghasilkan 10 karena integer dari string

data_float = float(data_str)
print(data_float)#akan menghasilkan 10.0 karena float dari string

data_bool = bool(data_str)
print(data_bool) #akan menghasilkan True karena string selain kosong adalah True


#boolean
data_bool = True
print(data_bool)

data_int = int(data_bool)
print(data_int)#akan menghasilkan 1 karena integer dari boolean

data_str = str(data_bool)
print(data_str)#akan menghasilkan 'True' karena string dari boolean

data_float = float(data_bool)
print(data_float)#akan menghasilkan 1.0 karena float dari boolean
