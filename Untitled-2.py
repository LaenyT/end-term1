import java.util.*;

public class alg {
    public static void main(String[] args) {
        ArrayList<Float> grades = new ArrayList<Float>();
        grades.add(3.3F);
        grades.add(2.7F);
        grades.add(4.0F);
        ArrayList<Integer> credits = new ArrayList<Integer>();
        credits.add(4);
        credits.add(3);
        credits.add(4);

        System.out.printf("%.2f" , calculateGPA(grades , credits));
    }
    private static float calculateGPA(ArrayList<Float> scores, ArrayList<Integer> credits){
        float gpa = 0.0F;
        int score = 0;
        float sum = 0.0F;
        for (int i = 0 ; i < scores.size() ; i++){
            sum += scores.get(i) * credits.get(i);
            score +=credits.get(i);
        }
        gpa = sum / score;
        return gpa;
    }

    private static ArrayList<Float> translateLetter(ArrayList<String> grades){
        ArrayList<Float> result = new ArrayList<Float>();
        Map<String, Float> gradePoints = new HashMap<>();

        gradePoints.put("A+", 4.3F);
        gradePoints.put("A", 4.0F);
        gradePoints.put("A-", 3.7F);
        gradePoints.put("B+", 3.3F);
        gradePoints.put("B", 3.0F);
        gradePoints.put("B-", 2.7F);
        gradePoints.put("C+", 2.3F);
        gradePoints.put("C", 2.0F);
        gradePoints.put("C-", 1.7F);
        gradePoints.put("D+", 1.3F);
        gradePoints.put("D", 1.0F);
        gradePoints.put("D-", 0.7F);
        for (int i = 0 ; i < grades.size() ; i++) {
            result.add(gradePoints.get(grades.get(i)));
        }
        return result;
    }
    private static ArrayList<Float> translatePercentage(ArrayList<Integer> percentage){
        ArrayList<Float> result = new ArrayList<Float>();
        
        for (int i = 0 ; i < percentage.size() ; i++) {
            result.add(getScore(percentage.get(i)));
        }
        return result;
    }

    private static Float getScore(Integer percentage) {
        if (percentage >= 95){
            return 4.7F;
        }else if (percentage >= 90 && percentage <= 94){
            return 4.0F;
        }else if (percentage >= 85 && percentage <= 89){
            return 3.7F;
        }else if (percentage >= 80 && percentage <= 84){
            return 3.3F;
        }else if (percentage >= 75 && percentage <= 79){
            return 3.0F;
        }else if (percentage >= 70 && percentage <= 74){
            return 2.7F;
        }else if (percentage >= 65 && percentage <= 69){
            return 2.3F;
        } else if (percentage >= 60 && percentage <= 64){
            return 2.0F;
        }else if (percentage >= 55 && percentage <= 59){
            return 1.7F;
        }else if (percentage >= 50 && percentage <= 54){
            return 1.3F;
        }else if (percentage >= 45 && percentage <= 49){
            return 1.0F;
        }else {
            return 0.7F;
        }
    }