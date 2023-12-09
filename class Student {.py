class Student {
    private String name;
    private int number_courses;
    private Map<String , Map<String , Integer>> scores;
    private float gpa;
    private String status;

    public  Student(){}

    private boolean setName(String name) {
        this.name = name;
        return  true;
    }

    private boolean setNumber_courses(int number_courses) {
        this.number_courses = number_courses;
        return true;
    }

    private boolean registerScores(String course_name , double course_score , int course_credits){
        return true;
    }

    public float calculateGPA(Map<String , Map<String , Integer>> scores){
        return 1.0F;
    }
    private void showGPA(){

    }
    public String setStatus(float gpa){
        return "";
    }

    private void showStatus(){}
    private void showScores(){}
}