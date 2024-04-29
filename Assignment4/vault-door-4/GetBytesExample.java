public class GetBytesExample {

    public static String backToString(byte[] bytes) {
        // byte[] bytes = {72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33};
        
        // Convert byte array to string using the platform's default charset
        String text = new String(bytes);
        
        // Display the resulting string
        //System.out.println(text);
        return text;
    }
    public static void main(String[] args) {
        String text = "LLN";
        
        // Convert the string to bytes using the default charset
        byte[] bytes = text.getBytes();
        
        // Display the byte array
        for (byte b : bytes) {
            System.out.print(b + " ");
        }
        System.out.println();
        String retString = backToString(bytes);
        System.out.println(retString);
    }
}
