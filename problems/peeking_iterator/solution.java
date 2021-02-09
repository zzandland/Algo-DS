// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> itr;
    Integer next;
    
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
        itr = iterator;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (next == null) next = itr.next();
        return (Integer)next;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
        if (next == null) return (Integer)itr.next();
        Integer res = next;
        next = null;
        return res;
	}
	
	@Override
	public boolean hasNext() {
        return itr.hasNext() || next != null;
	}
}