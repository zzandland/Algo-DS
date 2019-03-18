import java.util.regex.*;

class Solution {
  public List<String> subdomainVisits(String[] cpdomains) {
    Map<String, Integer> map = new HashMap<String, Integer>();
    for (String domain : cpdomains) {
      breakDomain(domain, map);
    }
    return mapToList(map);
  }
  
  private void breakDomain(String domain, Map<String, Integer> map) {
    Pattern visits = Pattern.compile("^(\\d+)(?:\\s)");
    Matcher m = visits.matcher(domain);
    if (m.find()) {
      int count = Integer.parseInt(m.group(1));
      String[] rest = domain.substring(m.end()).split("\\.");
      populateMap(count, rest, map);
    }
  }
  
  private void populateMap(int count, String[] domainArr, Map<String, Integer> map) {
    StringBuilder build = new StringBuilder();
    for (int i = domainArr.length - 1; i >= 0; i--) {
      build.insert(0, domainArr[i]);
      String currDomain = build.toString();
      if (map.containsKey(currDomain)) {
        map.put(currDomain, map.get(currDomain) + count);
      } else {
        map.put(currDomain, count);
      }
      build.insert(0, '.');
    }
  }
  
  private List<String> mapToList(Map<String, Integer> map) {
    List<String> list = new ArrayList<String>();
    for (Map.Entry<String, Integer> entry : map.entrySet()) {
      String result = entry.getValue() + " " + entry.getKey();
      list.add(result);
    }
    return list;
  }
}