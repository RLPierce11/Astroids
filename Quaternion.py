# class Quaternion file
#from Vector3n import Vector3n
import math

class Quaternion:
	def __init__(self, s, vect):
		self.s = s
		self.vect = vect

	def show(self):
		print("[" + str(round(self.s, 2)) + ", (" + str(round(self.vect.x, 2)) + ", " + str(round(self.vect.y, 2)) + ", " + str(round(self.vect.z, 2)) + ")]")

	#add quaternions
	def __add__(self, q1):
		s = self.s + q1.s
		imag = self.vect + q1.vect
		q = Quaternion(s, imag)
		return q
	def __IADD__(self, q):
		self.s += q.s
		self.vect += q.vect

	#subtract quaternions
	def __sub__(self, q1):
		s = self.s - q1.s
		imag = self.vect - q1.vect
		q = Quaternion(s, imag)
		return q
	def __ISUB__(self, q):
		self.s -= q.s
		self.vect -= q.vect

	#multiply quaternions
	def __mul__(self, q1):
		scaler = self.s * q1.s - self.vect.dot(q1.vect)
		imag = q1.vect.multS(self.s) + self.vect.multS(q1.s) + self.vect.cross(q1.vect)
		q = Quaternion(scaler, imag)
		return q
	def multiply(self, q1):
		scaler = self.s * q1.s - self.vect.dot(q1.vect)
		imag = q1.vect * self.s + self.vect * q1.s + self.vect.cross(q1.vect)
		q = Quaternion(scaler, imag)
		return q
	def __IMUL__(self, q1):
		self = self.multiply(q1)

	#scaler multiplication
	def multS(self, s):
		scaler = self.s * s
		imag = self.vect.multS(s)
		q = Quaternion(scaler, imag)
		return q
	def multS_S(self, s):
		self.s *= s
		self.vect.multS_S(s)

	#Norm
	def norm(self):
		scaler = self.s * self.s
		imag = self.vect * self.vect
		return math.sqrt(scaler + imag)

	#unit norm -> normalization
	def normalize(self):

		if(self.norm() != 0):
			normValue = 1 / self.norm()
			self.s *= normValue
			self.vect.multS_S(normValue)

	#unit norm quaternion special form
	def convertToUnitNormQ(self):
		angle = math.radians(self.s)
		self.vect.normalize()
		self.s = math.cos(angle * 0.5)
		self.vect = self.vect.multS(math.sin(angle * 0.5))

	#conjugate of quaternion
	def conjugate(self):
		imag = self.vect.multS(-1)
		q = Quaternion(self.s, imag)
		return q

	#inverse of quaternion
	def inverse(self):
		absolutValue = self.norm()
		absolutValue *= absolutValue
		absolutValue = 1 / absolutValue

		conjugateValue = self.conjugate()

		scaler = conjugateValue.s * absolutValue
		imag = conjugateValue.vect.multS(absolutValue)

		q = Quaternion(scaler, imag)
		return q

	#LERP-> linear quaternion interpolation
	def LERP(self, qend, t):
		q = (self.multS(1 - t) + (qend.multS(t)))
		#q.normalize()
		return q

	#SLERP->sqherical linear interpolation
	def SLERP(self, qend, t):
		mdot = self.s * qend.s + self.vect.x * qend.vect.x + self.vect.y * qend.vect.y + self.vect.z * qend.vect.z

		if(mdot < 0):
			mdot = -mdot
			q3 = qend.multS(-1)
		else:
			q3 = qend

		angle = math.cos(mdot)
		return (self.multS(math.sin(angle * (1 - t))) + q3.multS(math.sin(angle * t))).multS(1/math.sin(angle)) 

	#SLERP no INVERT
	def SLERPNoInvert(self, qend, t):
		mdot = self.s * qend.s + self.vect.x * qend.vect.x + self.vect.y * qend.vect.y + self.vect.z * qend.vect.z

		if(mdot > -0.95 and mdot < 0.95):
			angle = math.acos(mdot)
			return (self.multS(math.sin(angle * (1 - t))) + qend.multS(math.sin(angle * t))).multS(1/math.sin(angle))
		else:
			return self.LERP(qend, t)

	#quaternion logmarithic
	def Log(self):

		scaler = math.log(self.norm())
		vmag = self.vect.mag()
		oneOverMag = 1 / vmag
		sOverQNorm = self.s / self.norm()
		a = oneOverMag * math.acos(sOverQNorm)
		vect = self.vect
		vect.x = self.vect.x * a
		vect.y = self.vect.y * a
		vect.z = self.vect.z * a
		
		q = Quaternion(scaler, vect)
		return q


	#quaternion exponential
	def Exp(self):
		vNorm = self.vect.mag()
		sExp = math.exp(self.s)
		scale = sExp / vNorm * math.sin(vNorm)

		vect = self.vect

		if(vNorm):
			vect.x = 0
			vect.y = 0
			vect.z = 0
			q = Quaternion(sExp, vect)
			return q

		vect.x = self.vect.x * scale
		vect.y = self.vect.y * scale
		vect.z = self.vect.z * scale
		q = Quaternion(sExp * math.cos(vNorm), vect)
		return q


	#spline operation for SQUAD
	def spline(self, q1, q1n):
		q1Inverse = q1.inverse()
		log1 = q1Inverse * self
		log1 = log1.Log()
		log2 = q1Inverse * q1n
		log2 = log2.Log()
		qret = log1 + log2
		qret = qret.multS(1 / -4)
		qret.Exp()
		qret = qret * q1
		return qret

	#squad
	def squad(self, q2, a, b, t):
		c = self.SLERPNoInvert(q2, t)
		d = a.SLERPNoInvert(b, t)
		return c.SLERPNoInvert(d, 2 * t * (1 - t))

	#SQUAD
	def SQUAD(self, q1, q2, q3, t):
		a = self.spline(q1, q2)
		b = q1.spline(q2, q3)
		ret = self.squad(q3, a, b, t)
		return ret






