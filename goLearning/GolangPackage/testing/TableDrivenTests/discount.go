package store

func CalculatePrice(level string, price float64) float64 {
	switch level {
	case "VIP":
		return price * 0.8
	case "Admin":
		return price * 0.5
	default:
		return price
	}
}