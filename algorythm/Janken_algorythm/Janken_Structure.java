public class Janken_Structure {
    public static void main(String...args) {
        int gu = 1;
        int tyoki = 2;
        int pa = 3;

        int draw = 1;
        int win = 2;
        int lose = 3;

        int user = new java.util.Random.randint(3);
        int computer = new java.util.Random.randint(3);

        int judge[][] =  new int [3][3];

            judge[0][0] = draw;
            judge[0][1] = win;
            judge[0][2] = lose;

            judge[1][0] = lose;
            judge[1][1] = draw;
            judge[1][2] = win;

            judge[2][0] = win;
            judge[2][1] = lose;
            judge[2][2] = draw;



    }


}
