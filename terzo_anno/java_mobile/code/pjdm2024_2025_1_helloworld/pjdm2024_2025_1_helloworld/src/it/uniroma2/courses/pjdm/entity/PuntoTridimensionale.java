package it.uniroma2.courses.pjdm.entity;

import java.util.Objects;

public class PuntoTridimensionale extends Punto {

	private double z;

	public PuntoTridimensionale(double x, double y, double z) {
		super(x, y);
		this.z = z;
	}

	public double getZ() {
		return z;
	}

	public void setZ(double z) {
		this.z = z;
	}

	@Override
	public String toString() {
		return "PuntoTridimensionale [x=" + super.getX() + ", ...]";
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + Objects.hash(z);
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		PuntoTridimensionale other = (PuntoTridimensionale) obj;
		return Double.doubleToLongBits(z) == Double.doubleToLongBits(other.z);
	}

}
