def is_leap_year(year):
  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    try:
        
        year_input = input("请输入一个年份：")
        year = int(year_input)
        
        
        if is_leap_year(year):
            print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
    
    except ValueError:
        
        print(f"错误：'{year_input}'不是有效的年份，请输入一个整数。")

if __name__ == "__main__":
    main()

