import java.util.*;

public class MaximumClavier {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int temp;
        int max = scanner.nextInt();
        temp = scanner.nextInt();
        if (temp > max) {
            max = temp;
        }
        temp = scanner.nextInt();
        if (temp > max) {
            max = temp;
        }
        System.out.println(max+1);
    }

    public static void positionMax() {
        Scanner scanner = new Scanner(System.in);
        int pos = 0;
        int temp;
        int max = scanner.nextInt();
        temp = scanner.nextInt();
        if (temp > max) {
            max = temp;
            pos = 1;
        }
        temp = scanner.nextInt();
        if (temp > max) {
            pos = 2;
        }
        System.out.println(pos+1);
    }

    public static void affichageEnOrdre() {
        Scanner scanner = new Scanner(System.in);

        List<Integer> list = new ArrayList<>();
        list.add(scanner.nextInt());
        list.add(scanner.nextInt());
        list.add(scanner.nextInt());

        Collections.sort(list,Collections.reverseOrder());


        for(Integer i : list){
            System.out.print(""+i+" ");
        }
    }


}
