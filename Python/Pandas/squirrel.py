import pandas

data = pandas.read_csv("Squirrel_Data.csv")

squirrel_colors = data["Primary Fur Color"].dropna() # dropna drops nan values
squirrel_color_dict = {'Fur Color': [], 'Count': []}
for color in squirrel_colors.unique():
    # shape[0] gives number of rows in the dataframe
    # shape[1] will give number of columns
    num_colored_squirrel = data[ data["Primary Fur Color"] == color].shape[0]

    squirrel_color_dict["Fur Color"].append(color)
    squirrel_color_dict["Count"].append(num_colored_squirrel)

write_dataframe = pandas.DataFrame(squirrel_color_dict)
write_dataframe.to_csv('squirrel_color.csv')
