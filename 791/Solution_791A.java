import java.util.*;
public class Solution_791A{
    public static void main(String [] args){
        int a,b;
        int year = 0;
        Scanner s = new Scanner(System.in);
        a = s.nextInt();
        b = s.nextInt();
        while (a<=b){
            a = a*3;
            b = b*2;
            year = year+1;
        }
        System.out.println(year);
    }
}