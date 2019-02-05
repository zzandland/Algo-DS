import java.util.HashSet;

class Solution {
  public int numUniqueEmails(String[] emails) {
    HashSet emailSet = new HashSet();
    String regex = "(?x)\n"
      + "\\.|\\+.*      # match character '.' OR anything from character '+'";
    for (String email : emails) {
      if (email.equals("")) {
        emailSet.add("");
      } else {
        int index = email.indexOf("@");
        String local = email.substring(0, index);
        String domain = email.substring(index);
        StringBuilder build = new StringBuilder();
        build.append(local.replaceAll(regex, "")).append(domain);
        emailSet.add(build.toString());
      }
    }
    return emailSet.size();
  }
}