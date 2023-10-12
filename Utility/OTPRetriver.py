import imaplib
import email
import re


def otp_catcher_gmail(username, password):
    """Retrieves the latest OTP from a Gmail inbox.

    Args:
        username (str): The Gmail username.
        password (str): The Gmail password.

    Returns:
        str: The OTP, or None if no OTP was found.
    """

    try:
        # Connect to Gmail IMAP server
        imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
        imap_server.login(username, password)

        # Select the inbox
        imap_server.select('inbox')

        # Search for emails with a specific subject (e.g., "Rokomari Account Verification OTP")
        subject = 'Rokomari Account Verification OTP'
        result, data = imap_server.search(None, f'SUBJECT "{subject}"')

        # Get the email ID of the latest email with the matching subject
        email_ids = data[0].split()
        if email_ids:
            latest_email_id = email_ids[-1]
            result, message_data = imap_server.fetch(latest_email_id, '(RFC822)')
            raw_email = message_data[0][1]

            # Parse the email
            msg = email.message_from_bytes(raw_email)

            # Extract OTP using a refined regular expression
            otp_pattern = r'(\d{4})\b'
            otp_match = ''.join(re.findall(otp_pattern, msg.get("Subject", "")))

            if otp_match:
                otp = otp_match
                return otp
            else:
                return None

        else:
            return None

    except Exception as e:
        # Handle any errors
        print(f'Error retrieving OTP: {e}')
        return None

    finally:
        # Close the IMAP connection
        imap_server.logout()
