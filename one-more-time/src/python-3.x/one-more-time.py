def main():
    target_degree = int(input("Target degree: "))
    x_points = []
    y_points = []

    # input
    for i in range(target_degree + 1):
        xi = float(input("x%d = " % i))
        yi = float(input("y%d = " % i))

        x_points.append(xi)
        y_points.append(yi)

    lagrange_sums = []
    for i in range(len(x_points)):
        constant = y_points[i]

        lagrange_terms = []
        for j in range(len(x_points)):
            if i == j:
                continue
            else:
                constant /= x_points[i] - x_points[j]
                if len(lagrange_terms) == 0:
                    lagrange_terms = [1, - x_points[j]]
                else:
                    temp = list(lagrange_terms)
                    lagrange_terms.append(0)

                    for k in range(len(temp)):
                        temp[k] *= - x_points[j]
                        lagrange_terms[k + 1] += temp[k]

        lagrange_terms = map(lambda x: x * constant, lagrange_terms)
        if len(lagrange_sums) == 0:
            lagrange_sums = list(lagrange_terms)
        else:
            lagrange_sums = [sum(i) for i in zip(lagrange_sums, lagrange_terms)]
    

    for i, a in enumerate(lagrange_sums):
        if a != 0:
            print(f"({a})", end="")

            if target_degree - i != 0:
                print(f"X^{target_degree - i} + ", end="")
    print()




        


if __name__ == "__main__":
    main()