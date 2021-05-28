class GeoObj {
	abstract commutative double distanceTo(GeoObj b);
	commutative boolean distanceIsLessThan(GeoObj g, double d) {
		return this.distanceTo(g) < d;
	}
}

class Point extends GeoObj {
	commutative double distanceTo(Point b);
}

class Line extends GeoObj {
	commutative double distanceTo(Point b);
	commutative double distanceTo(Line b);
}

class WeirdShape extends GeoObj {
	Point[] subshape;
	commutative boolean distanceIsLessThan(GeoObj g, double d) {
		double modified_distace = d**3 + d;
		for(Point p : this.subshape) {
			if(p.distanceIsLessThan(g, modified_distace)) {
				return true;
			}
		}
		return false;
	}
	distanceIsLessThan : (GeoObj, double) -> boolean === GeoObj -> double -> boolean
	commutative (GeoObj -> boolean) distanceIsLessThan(double d) {
		double modified_distace = d**3 + d;
		return double lambda(GeoObj g) {
			for(Point p : this.subshape) {
				if(p.distanceIsLessThan(g, modified_distace)) {
					return true;
				}
			}
			return false;
		}
	}
}

w = WeirdShape()
fn1 = w.distanceIsLessThan(d)
print(fn1(g))
fn2 = w.distanceIsLessThan(g)
print(fn2(d))


p = new Point()
l = new Line()
p.distanceTo(l) // Undefined
p.distanceTo(l) === GeoObj.distanceTo(p, l) === GeoObj.distanceTo(l, p) === l.distanceTo(p)
p.distanceIsLessThan(l, 0.1)

g = new GeoObj()
p.distanceIsLessThan(0.1, g)

isCloseToP = p.distanceIsLessThan(0.1)
isCloseToP(l)
q = new Point()
isCloseToP(q)



intersects: (GeoObj, GeoObj) -> boolean


class GeoObj {
	boolean intersects
}
