import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

/**
 * OneMoreTime
 */
public class OneMoreTime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input target degree: ");
        int target_degree = sc.nextInt();

        List<Double> xPoints = new ArrayList<Double>();
        List<Double> yPoints = new ArrayList<Double>();

        System.out.println("Input xi yi");
        for (int i = 0; i <= target_degree; i++) {
            double xi = sc.nextDouble();
            double yi = sc.nextDouble();
            xPoints.add(xi);
            yPoints.add(yi);
        }

        List<Double> interpolation = new ArrayList<>();
        for (int i = 0; i < xPoints.size(); i++) {
            double constant = yPoints.get(i);
    
            List<Double> lagrange_terms = new ArrayList<>();
            for (int j = 0; j < xPoints.size(); j++) {
                if (i != j) {
                    constant /= xPoints.get(i) - xPoints.get(j);

                    if (lagrange_terms.isEmpty()) {
                        lagrange_terms.add(1.0);
                        lagrange_terms.add(-xPoints.get(j));
                    } else {
                        List<Double> multiplier = new ArrayList<>(lagrange_terms);
                        lagrange_terms.add(0.0);
    
                        for (int k = 0; k < multiplier.size(); k++) {
                            multiplier.set(k, multiplier.get(k) * -xPoints.get(j));
                            lagrange_terms.set(k + 1, lagrange_terms.get(k + 1) + multiplier.get(k));
                        }
                    }
                }
            }
            for (int j = 0; j < lagrange_terms.size(); j++) {
                lagrange_terms.set(j, lagrange_terms.get(j) * constant);
            }
            
            if (interpolation.isEmpty()) {
                interpolation = new ArrayList<>(lagrange_terms);
            } else {
                for (int j = 0; j < interpolation.size(); j++) {
                    interpolation.set(j, interpolation.get(j) + lagrange_terms.get(j));
                }
            }
        }

        System.out.println("Coeff       |       Degree");
        int degree = target_degree;
        for (Double ax : interpolation) {
            System.out.print(ax);
            System.out.println("    |   " + degree);
            degree--;
        }
        
        sc.close();
    }
}