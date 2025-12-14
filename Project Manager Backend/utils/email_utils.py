# utils/email_utils.py
import secrets
from flask_mail import Message
from flask import current_app
from app import mail


def generate_invitation_token():
    return secrets.token_urlsafe(32)


def send_invitation_email(admin_name, member_email, project_name, invitation_token):
    # Create invitation link
    invitation_link = f"{current_app.config.get('FRONTEND_URL', 'http://localhost:5173')}/register?token={invitation_token}"

    # Create email message
    subject = f"Invitation to join project: {project_name}"

    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(to right, #4f46e5, #7c3aed); color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9fafb; padding: 30px; border-radius: 0 0 10px 10px; }}
            .button {{ display: inline-block; background: #4f46e5; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; }}
            .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e7eb; color: #6b7280; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Project Management Invitation</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p><strong>{admin_name}</strong> has invited you to join the project: <strong>{project_name}</strong>.</p>
                <p>Click the button below to accept the invitation and create your account:</p>
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{invitation_link}" class="button">Accept Invitation</a>
                </div>
                <p>This invitation link will expire in 7 days.</p>
                <p>If you didn't expect this invitation, you can safely ignore this email.</p>
                <div class="footer">
                    <p>Best regards,<br>Project Management Team</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    msg = Message(
        subject=subject,
        recipients=[member_email],
        html=html_body,
        sender=current_app.config.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')
    )

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False