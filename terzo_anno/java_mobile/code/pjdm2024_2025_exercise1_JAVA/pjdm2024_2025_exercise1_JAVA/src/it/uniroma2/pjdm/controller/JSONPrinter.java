package it.uniroma2.pjdm.controller;

import org.json.JSONException;
import org.json.JSONObject;

public interface JSONPrinter {

	/**
	 * Generate a JSONObject reflecting the content of the object.
	 * 
	 * @return A JSONObject reflecting the content of the object
	 * @throws JSONException This exception is thrown when the conversion is not
	 *                       possible
	 */
	public JSONObject getJSONObject() throws JSONException;
}
