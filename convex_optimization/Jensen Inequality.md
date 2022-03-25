# Jensen 不等式

## 1、凸函数

凸函数是一个定义在某个向量空间的凸子集 C（区间）上的实值函数 f，如果在其定义域 C 上的任意两点 $x_1,x_2$ ，$0\leq t \leq 1$，有
$$
t f\left(x_{1}\right)+(1-t) f\left(x_{2}\right) \geq f\left(t x_{1}+(1-t) x_{2}\right)
$$
也就是说凸函数任意两点的割线位于函数图形上方， **这也是Jensen不等式的两点形式**。

## 2、Jensen不等式

若对于任意点集 $\{x_i\}$，若 $\lambda_{i} \geq 0$ 且$\sum_{i} \lambda_{i}=1$，使用**数学归纳法**，可以证明凸函数 f (x) 满足：
$$
f\left(\sum_{i=1}^{M} \lambda_{i} x_{i}\right) \leq \sum_{i=1}^{M} \lambda_{i} f\left(x_{i}\right)
$$
该公式被称为 Jensen 不等式，当**f(x)为常数**时等号成立。

证明如下：

当i=1或2时，由凸函数的定义成立；假设当i=M时，Jensen 不等式成立，现在证明则i=M+1时，Jensen不等式也成立：
$$
\begin{array}{l}
f\left(\sum_{i=1}^{M+1} \lambda_{i} x_{i}\right)=f\left(\lambda_{M+1} x_{M+1}+\sum_{i=1}^{M} \lambda_{i} x_{i}\right) \\
=f\left(\lambda_{M+1} x_{M+1}+\left(1-\lambda_{M+1}\right) \sum_{i=1}^{M} \eta_{i} x_{i}\right)
\end{array}
$$
其中：
$$
\eta_{i}=\frac{\lambda_{i}}{1-\lambda_{M+1}}
$$
根据凸函数的定义，我们可以得到：

$$
\left.f\left(\sum_{i=1}^{M+1} \lambda_{i} x_{i}\right) \leq \lambda_{M+1} f\left(x_{M+1}\right)+\left(1-\lambda_{M+1}\right) f\left(\sum_{i=1}^{M} \eta_{i} x_{i}\right)\right)
$$

注意到$\lambda_i$满足:
$$
\sum_{i=1}^{M+1}\lambda_i  = 1
$$
因此：
$$
\sum_{i=1}^{M}\lambda_i  = 1-\lambda_{M+1}
$$

因此 $\eta_i$满足：
$$
\sum_{i}^{M} \eta_{i}=\frac{\sum_{i}^{M} \lambda_{i}}{1-\lambda_{M+1}}=1
$$
所以有：
$$
\sum_{i=1}^{M} f\left(\eta_{i} x_{i}\right) \leq \sum_{i=1}^{M} \eta_{i} f\left(x_{i}\right)
$$
综上有：
$$
f\left(\sum_{i=1}^{M+1} \lambda_{i} x_{i}\right) \leq \lambda_{M+1} f\left(x_{M+1}\right)+\left(1-\lambda_{M+1}\right) \sum_{i=1}^{M} \eta_{i} f\left(x_{i}\right)=\sum_{i=1}^{M+1} \lambda_{i} f\left(x_{i}\right)
$$
因此i=M+1时，Jensen不等式也成立，综上，Jensen不等式成立。

**在概率论中**，如果把$\lambda_i$看成取值为$x_i$的离散变量 x 的概率分布，那么Jenson不等式就可以写成\
$$
f\left(E[x] \right) \leq E[f\left(x\right)]
$$
其中, $E()$表示期望。

对于连续变量，Jensen不等式给出了积分的凸函数值和凸函数的积分值间的关系：
$$
f\left(\int x p(x) d x\right) \leq \int f(x) p(x) d x
$$

Jensen 不等式也适用于凹函数（concave）$f$，但不等式的方向要反过来，也就是对于凹函数，$E[f(X)] \le f(EX)$。

**参考文献：**

[知乎 清雅的数学笔记](https://zhuanlan.zhihu.com/p/39315786#:~:text=Jensen%E4%B8%8D%E7%AD%89%E5%BC%8F%EF%BC%88Jensen%27s%20inequality%EF%BC%89%E6%98%AF%E4%BB%A5%E4%B8%B9%E9%BA%A6%E6%95%B0%E5%AD%A6%E5%AE%B6Johan,Jensen%E5%91%BD%E5%90%8D%E7%9A%84%EF%BC%8C%E5%AE%83%E5%9C%A8%E6%A6%82%E7%8E%87%E8%AE%BA%E3%80%81%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E3%80%81%E6%B5%8B%E5%BA%A6%E8%AE%BA%E3%80%81%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86%E7%AD%89%E9%A2%86%E5%9F%9F%E9%83%BD%E6%9C%89%E7%9B%B8%E5%85%B3%E5%BA%94%E7%94%A8%E3%80%82%20%E5%9C%A8%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A2%86%E5%9F%9F%EF%BC%8C%E6%88%91%E7%9B%AE%E5%89%8D%E6%8E%A5%E8%A7%A6%E5%88%B0%E7%9A%84%E6%98%AF%E7%94%A8Jensen%E4%B8%8D%E7%AD%89%E5%BC%8F%E7%94%A8%E6%9D%A5%E8%AF%81%E6%98%8EKL%E6%95%A3%E5%BA%A6%E5%A4%A7%E4%BA%8E%E7%AD%89%E4%BA%8E0%20%EF%BC%88%E4%BB%A5%E5%90%8E%E5%86%99%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E6%80%BB%E7%BB%93%E4%B8%80%E4%B8%8B%EF%BC%89%E3%80%82)