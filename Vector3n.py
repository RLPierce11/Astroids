
import math
from Quaternion import Quaternion

#class Vector3n file
class Vector3n:
	def __init__(self, ux, uy, uz):
		self.x = ux
		self.y = uy
		self.z = uz
	
	#print vector 	
	def show(self):
		print("[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]")
	
	#add two vectors
	def add(self, vect):
		vector = Vector3n(self.x + vect.x, self.y + vect.y, self.z + vect.z)
		return vector 
	def __add__(self, vect):
		vector = Vector3n(self.x + vect.x, self.y + vect.y, self.z + vect.z)
		return vector 
	#add vector to self
	def __IADD__(self, vect):
		self.x += vect.x
		self.y += vect.y
		self.z += vect.z

	#subtract two vectors
	def sub(self, vect):
		vector = Vector3n(self.x - vect.x, self.y - vect.y, self.z - vect.z)
		return vector
	def __sub__(self, vect):
		vector = Vector3n(self.x - vect.x, self.y - vect.y, self.z - vect.z)
		return vector
	#subtract vector to self
	def __ISUB__(self, vect):
		self.x -= vect.x
		self.y -= vect.y
		self.z -= vect.z

	#multiply by scaler
	def multS(self, s):
		vector = Vector3n(self.x * s, self.y * s, self.z * s)
		return vector
	#def __mul__(self, s):
		#vector = Vector3n(self.x * s, self.y * s, self.z * s)
		#return vector
	#multiply scaler to itself
	#def __IMUL__(self, s):
		#self.x *= s
		#self.y *= s
		#self.z *= s
	def multS_S(self, s):
		self.x *= s
		self.y *= s
		self.z *= s

	#divide by scaler
	def div(self, s):
		vector = Vector3n(self.x / s, self.y / s, self.z / s)
		return vector
	def __truediv__(self, s):
		vector = Vector3n(self.x / s, self.y / s, self.z / s)
		return vector
	#dive self by scaler
	def __IDIV__(self, s):
		self.x /= s
		self.y /= s
		self.z /= s


	#multiply two vectors dot product
	def dot(self, vect):
		return self.x * vect.x + self.y * vect.y + self.z * vect.z
		
	def __mul__(self, vect):
		return self.x * vect.x + self.y * vect.y + self.z * vect.z


	#cross product of two vectors
	def cross(self, vect):
		vector = Vector3n(self.y * vect.z - self.z * vect.y,
						  self.z * vect.x - self.x * vect.z,
						  self.x * vect.y - self.y * vect.x)
		return vector
	def __mod__(self, vect):
		vector = Vector3n(self.y * vect.z - self.z * vect.y,
						  self.z * vect.x - self.x * vect.z,
						  self.x * vect.y - self.y * vect.x)
		return vector
	#multiply vector to itself dot product
	def __IMOD__(self, vect):
		self.x = self.y * vect.z - self.z * vect.y
		self.y = self.z * vect.x - self.x * vect.z
		self.z = self.x * vect.y - self.y * vect.x

	#magnitude of vector
	def mag(self):
		m = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
		return m

	#normalize vector
	def normalize(self):
		mag = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

		if(mag > 0.0):
			oneOverMag = 1.0 / mag
			self.x = self.x * oneOverMag
			self.y = self.y * oneOverMag
			self.z = self.z * oneOverMag

	#rotate vector using Quaternion
	def rotateVector(self, angle, axis):
		#convert current vector to pure quaternion
		pure = Quaternion(0, self)
		#normalize axis input
		axis.normalize()
		#create real quaternion using input angle=scaler and axis=vector
		rquat = Quaternion(angle, axis)
		#convert real quaternion to norm quaternion
		rquat.convertToUnitNormQ()
		#get the inverse of real quaternion
		qInverse = rquat.inverse()
		#rotate the quaternion
		rotatedVector = rquat * pure * qInverse

		rvect = Vector3n(round(rotatedVector.vect.x, 2), round(rotatedVector.vect.y, 2), round(rotatedVector.vect.z, 2))
		#return vector of the rotated quaternion
		return rvect

	#rotate vector using Quaternion LERP
	def rotateVectorLERP(self, angle, axis, t):
		#convert current vector to pure quaternion
		pure = Quaternion(0, self)
		#normalize axis input
		axis.normalize()
		#create real quaternion using input angle=scaler and axis=vector
		rquat = Quaternion(angle, axis)
		#convert real quaternion to norm quaternion
		rquat.convertToUnitNormQ()
		#get the inverse of real quaternion
		qInverse = rquat.inverse()
		#rotate the quaternion
		rotatedVector = rquat * pure * qInverse

		qlerp = pure.LERP(rotatedVector, t)

		rvect = Vector3n(round(qlerp.vect.x, 2), round(qlerp.vect.y, 2), round(qlerp.vect.z, 2))
		#return vector of the rotated quaternion
		return rvect

	#rotate vector using Quaternion SLERP
	def rotateVectorSLERP(self, angle, axis, t):
		#convert current vector to pure quaternion
		pure = Quaternion(0, self)
		#normalize axis input
		axis.normalize()
		#create real quaternion using input angle=scaler and axis=vector
		rquat = Quaternion(angle, axis)
		#convert real quaternion to norm quaternion
		rquat.convertToUnitNormQ()
		#get the inverse of real quaternion
		qInverse = rquat.inverse()
		#rotate the quaternion
		rotatedVector = rquat * pure * qInverse

		qslerp = pure.SLERP(rotatedVector, t)

		rvect = Vector3n(round(qslerp.vect.x, 2), round(qslerp.vect.y, 2), round(qslerp.vect.z, 2))
		#return vector of the rotated quaternion
		return rvect

	#rotate vector using Quaternion SLERP no invert
	def rotateVectorSLERPNoInvert(self, angle, axis, t):
		#convert current vector to pure quaternion
		pure = Quaternion(0, self)
		#normalize axis input
		axis.normalize()
		#create real quaternion using input angle=scaler and axis=vector
		rquat = Quaternion(angle, axis)
		#convert real quaternion to norm quaternion
		rquat.convertToUnitNormQ()
		#get the inverse of real quaternion
		qInverse = rquat.inverse()
		#rotate the quaternion
		rotatedVector = rquat * pure * qInverse

		qslerpN = pure.SLERPNoInvert(rotatedVector, t)

		rvect = Vector3n(round(qslerpN.vect.x, 2), round(qslerpN.vect.y, 2), round(qslerpN.vect.z, 2))
		#return vector of the rotated quaternion
		return rvect

	#rotate vector using Quaternion SQUAD
	def rotateVectorSQUAD(self, angle, axis, t):
		#convert current vector to pure quaternion
		pure = Quaternion(0, self)
		#normalize axis input
		axis.normalize()
		#create real quaternion using input angle=scaler and axis=vector
		rquat = Quaternion(angle, axis)
		#convert real quaternion to norm quaternion
		rquat.convertToUnitNormQ()
		#get the inverse of real quaternion
		qInverse = rquat.inverse()
		#rotate the quaternion
		rotatedVector = rquat * pure * qInverse

		q1 = pure.SLERP(rotatedVector, 0.25)
		q2 = pure.SLERP(rotatedVector, 0.75)

		qsquad = pure.SQUAD(q1, q2, rotatedVector, t)

		rvect = Vector3n(round(qsquad.vect.x, 2), round(qsquad.vect.y, 2), round(qsquad.vect.z, 2))
		#return vector of the rotated quaternion
		return rvect

	#translate vector to origin and rotate vector and return
	def rotate(self, origin, angle):
		tvect = Vector3n(self.x - origin.x, self.y - origin.y, 0)
		axis = Vector3n(0, 0, 1)
		tvect = tvect.rotateVector(angle, axis)
		return origin + tvect


