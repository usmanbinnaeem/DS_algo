public class ClassNameHere {
    /** Returns the maximum value from m. */
    public static int max(int[] m) {
        int maxi = 0;
       for(int i = 0; i < m.length; i++){
           if(m[i] > maxi){
               maxi = m[i];
           }
       }
        System.out.println(maxi);
        return 0;
    }
    public static void main(String[] args) {
       int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
       max(numbers);
    }
}