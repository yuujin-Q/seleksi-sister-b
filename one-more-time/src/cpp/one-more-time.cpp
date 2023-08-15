#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int target_degree;
    cout << "Input target degree: ";
    cin >> target_degree;

    vector<double> x_points;
    vector<double> y_points;

    cout << "Input xi yi" << endl;
    for (int i = 0; i <= target_degree; i++) {
        double xi, yi;
        cin >> xi >> yi;
        x_points.push_back(xi);
        y_points.push_back(yi);
    }

    vector<double> lagrange_sums;
    for (int i = 0; i < x_points.size(); i++) {
        double constant = y_points[i];

        vector<double> lagrange_terms;
        for (int j = 0; j < x_points.size(); j++) {
            if (i != j) {
                constant /= x_points[i] - x_points[j];
                if (lagrange_terms.empty()) {
                    lagrange_terms.push_back(1);
                    lagrange_terms.push_back(-x_points[j]);
                } else {
                    vector<double> temp(lagrange_terms);
                    lagrange_terms.push_back(0);

                    for (int k = 0; k < temp.size(); k++) {
                        temp[k] *= -x_points[j];
                        lagrange_terms[k + 1] += temp[k];
                    }
                }
            }
        }
        
        transform(lagrange_terms.begin(), lagrange_terms.end(), lagrange_terms.begin(), 
                  [constant](double val) { return val * constant; });

        if (lagrange_sums.empty()) {
            lagrange_sums = vector<double>(lagrange_terms);
        } else {
            transform(lagrange_sums.begin(), lagrange_sums.end(), lagrange_terms.begin(), lagrange_sums.begin(), plus<double>());
        }
    }
    
    int degree = target_degree;
    for (double term : lagrange_sums) {
        if (term != 0) {
            cout << "(" << term << ")";
            if (degree != 0) {
                cout << "X^" << degree << " + ";
            }
        }
        degree--;
    }
    cout << endl;
    
    return 0;
}