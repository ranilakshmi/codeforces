import java.util.*;
public class Solution_344A{
    public static void main(String [] args){
        int n;
        int group = 1;
        String a,b;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        a = input.next();
        for (int i=1;i<n;i++){
            b = a;
            a = input.next();
            if (!a.equals(b)){
                group = group +1;
            }
        }
        System.out.println(group);
    }
}