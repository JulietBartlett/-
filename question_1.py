# -*- coding: utf-8 -*-
import math
import sys
import io

def master_theorem_solver(a, b, f_degree, f_log_degree=0):
    """
    根据主定理求解 T(n) = aT(n/b) + O(n^d * log^k(n))
    其中 a >= 1, b > 1, f_degree = d, f_log_degree = k
    """
    log_b_a = math.log(a, b)
    
    print(f"步骤 1: 确定 a, b 和 f(n) 的复杂度参数:")
    print(f"        a = {a}, b = {b}, f(n) 的多项式阶数 d = {f_degree}")
    print(f"步骤 2: 计算临界值 n^(log_b(a)):")
    print(f"        log_{b}({a}) = {log_b_a:.4f} -> n^{log_b_a:.4f}")
    
    print(f"步骤 3: 比较 f(n) 和 n^(log_b(a)):")
    if f_degree < log_b_a - 1e-9:
        print(f"        由于 f(n) = O(n^{f_degree}) 渐近严格小于 n^{log_b_a:.4f}")
        print(f"        应用主定理情况 1 (Case 1)")
        if log_b_a.is_integer():
            ans = f"Θ(n^{int(log_b_a)})"
        else:
            ans = f"Θ(n^(log_{b}({a})))"
        print(f"结果:   T(n) = {ans}\n")
        return ans
    elif abs(f_degree - log_b_a) < 1e-9:
        print(f"        由于 f(n) 与 n^{log_b_a:.4f} 渐近同阶 (阶数相等)")
        print(f"        应用主定理情况 2 (Case 2)")
        new_log_deg = f_log_degree + 1
        
        if log_b_a == 0:
            p_base = ""
        elif log_b_a.is_integer():
            p_base = f"n^{int(log_b_a)}"
        else:
            p_base = f"n^{log_b_a:.4f}"
            
        p_log = f"log n" if new_log_deg == 1 else f"log^{new_log_deg} n"
        
        if p_base and p_log:
            ans = f"Θ({p_base} * {p_log})"
        elif p_base:
            ans = f"Θ({p_base})"
        else:
            ans = f"Θ({p_log})"
            
        print(f"结果:   T(n) = {ans}\n")
        return ans
    else:
        print(f"        由于 f(n) = Ω(n^{f_degree}) 渐近严格大于 n^{log_b_a:.4f}，且满足正则条件")
        print(f"        应用主定理情况 3 (Case 3)")
        ans = f"Θ(n^{f_degree})" if f_log_degree == 0 else f"Θ(n^{f_degree} * log^{f_log_degree} n)"
        print(f"结果:   T(n) = {ans}\n")
        return ans

def print_solutions():
    print("="*40)
    print("1. 计算 T(n) = T(n/4) + 1")
    print("="*40)
    master_theorem_solver(a=1, b=4, f_degree=0)
    
    print("="*40)
    print("2. 计算 T(n) = 3T(n/3) + n^2")
    print("="*40)
    master_theorem_solver(a=3, b=3, f_degree=2)
    
    print("="*40)
    print("3. 计算 T(n) = T(2n/3) + 1")
    print("="*40)
    # T(n) = T(n / (3/2)) + 1
    master_theorem_solver(a=1, b=1.5, f_degree=0)
    
    print("="*40)
    print("4. 计算 T(n) = 5T(n/4) + n")
    print("="*40)
    master_theorem_solver(a=5, b=4, f_degree=1)
    
    print("="*40)
    print("5. 计算 T(n) = T(√n) + 1")
    print("="*40)
    print("步骤 1: 观察到此方程不能直接套用主定理，通过变量代换将其转换为可使用主定理的形式。")
    print("        令 n = 2^m，此时 m = log_2(n)。")
    print("        原等式代入得：T(2^m) = T(2^(m/2)) + 1")
    print("步骤 2: 建立新的函数 S(m) = T(2^m)。")
    print("        可得递归式：S(m) = S(m/2) + 1")
    print("步骤 3: 对 S(m) 应用主定理:")
    master_theorem_solver(a=1, b=2, f_degree=0)
    print("步骤 4: 回代变量 m = log_2(n)。")
    print("        由于 S(m) = Θ(log m)")
    print("结果:   T(n) = Θ(log(log n))\n")

if __name__ == '__main__':
    # 强制标准输出使用 utf-8 编码，防止在 Windows 终端中出现中文乱码或无输出
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    else:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print_solutions()

