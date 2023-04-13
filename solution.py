
import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 700775408 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Вычисляем доли продаж
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
   
    # Вычисляем стандартную ошибку разности долей
    P = (x_success + y_success) / (x_cnt + y_cnt)
    SE = np.sqrt(P*(1-P)*(1/x_cnt + 1/y_cnt))

    # Вычисляем z-статистику
    z = (p2 - p1) / SE

    # Вычисляем критическое значение z-статистики
    z_crit = norm.ppf(1-alpha/2)

    # Сравниваем с критическим значением z_crit
    if z > z_crit:
        return True
    else:
        return False 
