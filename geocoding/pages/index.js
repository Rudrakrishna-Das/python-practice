import { useState, useEffect } from "react";
import dynamic from "next/dynamic";

// Dynamically import the map component with no SSR
const MapRender = dynamic(() => import("./MapComponent"), {
  ssr: false,
  loading: () => (
    <div
      style={{
        height: "400px",
        backgroundColor: "#f0f0f0",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginTop: "20px",
        border: "2px solid #ddd",
        borderRadius: "8px",
      }}
    >
      <div style={{ textAlign: "center" }}>
        <div style={{ fontSize: "32px", marginBottom: "10px" }}>🗺️</div>
        <div style={{ color: "#666", fontSize: "16px" }}>Loading Map...</div>
      </div>
    </div>
  ),
});

export default function Home() {
  const [formData, setFormData] = useState({
    address: "",
    gp: "",
    subdivision: "",
    block: "",
    district: "",
    city: "",
    state: "",
    country: "",
    pincode: "",
  });

  const [coordinates, setCoordinates] = useState(null);
  const [typingTimeout, setTypingTimeout] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    const newData = { ...formData, [name]: value };
    setFormData(newData);

    // Debounce geocoding call
    if (typingTimeout) clearTimeout(typingTimeout);
    const timeout = setTimeout(() => {
      geocodeAddress(newData);
    }, 700); // Wait 700ms after user stops typing
    setTypingTimeout(timeout);
  };
  const stripHouseNumber = (address) => {
    // Remove patterns like 41/2, 12A, 101-B, etc.
    return address.replace(/^\s*\d+[\/\-]?[A-Za-z0-9]*\s*/, "").trim();
  };

  const getFullAddress = (data) => {
    const cleanedAddress = stripHouseNumber(data.address);
    const fullAddress = [cleanedAddress, data.city, data.state, data.country]
      .filter(Boolean)
      .join(", ");

    return fullAddress;
  };

  const geocodeAddress = async (data) => {
    const sanitizeAddress = (str) =>
      str.replace(/[\n\r\/\\#@!$%^&*()+=<>[\]{}|`~]/g, "").trim();

    const fullAddress = sanitizeAddress(getFullAddress(data));
    console.log(fullAddress);
    if (!fullAddress.trim()) {
      setCoordinates(null);
      setError(null);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      console.log("Trying full address:", fullAddress);

      let response = await fetch(
        `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(
          fullAddress
        )}&limit=1`
      );
      let result = await response.json();

      if (!result.length) {
        // Try fallback address
        const fallbackAddress = [data.city, data.state, data.country]
          .filter(Boolean)
          .join(", ");
        console.log("Full address failed, trying fallback:", fallbackAddress);

        response = await fetch(
          `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(
            fallbackAddress
          )}&limit=1`
        );
        result = await response.json();
      }

      if (result.length) {
        const lat = parseFloat(result[0].lat);
        const lon = parseFloat(result[0].lon);
        if (!isNaN(lat) && !isNaN(lon)) {
          setCoordinates([lat, lon]);
          console.log("Found coordinates:", [lat, lon]);
        } else {
          setError("Invalid coordinates received.");
          setCoordinates(null);
        }
      } else {
        setError("Location not found.");
        setCoordinates(null);
      }
    } catch (err) {
      console.error("Geocoding error:", err);
      setError(`Error: ${err.message}`);
      setCoordinates(null);
    } finally {
      setIsLoading(false);
    }
  };

  // Cleanup timeout on unmount
  useEffect(() => {
    return () => {
      if (typingTimeout) {
        clearTimeout(typingTimeout);
      }
    };
  }, [typingTimeout]);

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
      <h2 style={{ color: "#333", marginBottom: "20px" }}>
        Enter Location (Map auto-updates)
      </h2>

      {/* Status Messages */}
      {isLoading && (
        <div
          style={{
            padding: "10px",
            backgroundColor: "#e3f2fd",
            border: "1px solid #2196f3",
            borderRadius: "4px",
            marginBottom: "15px",
            color: "#1976d2",
          }}
        >
          🔍 Searching for location...
        </div>
      )}

      {error && (
        <div
          style={{
            padding: "10px",
            backgroundColor: "#ffebee",
            border: "1px solid #f44336",
            borderRadius: "4px",
            marginBottom: "15px",
            color: "#c62828",
          }}
        >
          ⚠️ {error}
        </div>
      )}

      {coordinates && !isLoading && (
        <div
          style={{
            padding: "10px",
            backgroundColor: "#e8f5e8",
            border: "1px solid #4caf50",
            borderRadius: "4px",
            marginBottom: "15px",
            color: "#2e7d32",
          }}
        >
          ✅ Location found! Coordinates: {coordinates[0].toFixed(4)},{" "}
          {coordinates[1].toFixed(4)}
        </div>
      )}

      {/* Form Fields */}
      {[
        "address",
        "gp",
        "subdivision",
        "block",
        "district",
        "city",
        "state",
        "country",
        "pincode",
      ].map((field) => (
        <input
          key={field}
          name={field}
          value={formData[field]}
          onChange={handleChange}
          placeholder={field.charAt(0).toUpperCase() + field.slice(1)}
          style={{
            display: "block",
            marginBottom: "10px",
            padding: "10px",
            width: "100%",
            maxWidth: "400px",
            border: "1px solid #ccc",
            borderRadius: "4px",
            fontSize: "16px",
            outline: "none",
            transition: "border-color 0.2s",
          }}
          onFocus={(e) => (e.target.style.borderColor = "#2196f3")}
          onBlur={(e) => (e.target.style.borderColor = "#ccc")}
        />
      ))}

      {/* Current Address Display */}
      {getFullAddress(formData) && (
        <div
          style={{
            marginTop: "15px",
            marginBottom: "15px",
            padding: "12px",
            backgroundColor: "#f5f5f5",
            border: "1px solid #ddd",
            borderRadius: "6px",
          }}
        >
          <strong>Current Address: </strong>
          {getFullAddress(formData)}
        </div>
      )}

      {/* Map Component */}
      <MapRender coordinates={coordinates} setCoordinates={setCoordinates} />

      <div
        style={{
          marginTop: "10px",
          fontSize: "12px",
          color: "#666",
          textAlign: "center",
        }}
      >
        Powered by OpenStreetMap Nominatim
      </div>
    </div>
  );
}
